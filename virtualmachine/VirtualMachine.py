from typing import List
from util.utils import operator_from_symbol
from semantics.semantic_analyser import SymbolTable
import copy


class VirtualMachine:
    classes_memory = {}
    fun_stack = []
    obj_const_stack = []
    current_class_mem = None

    def __init__(self, quadruples: List, symbol_tables: List[SymbolTable]):
        self.quadruples = quadruples
        self.symbol_tables = symbol_tables

    def current_sym_table(self):
        return self.symbol_tables[len(self.symbol_tables) - 1]

    def current_mem(self):
        '''
        Returns the memory of the current active function, or the global if there are no funs in the stack.
        '''
        if len(self.fun_stack) > 0:
            return self.fun_stack[len(self.fun_stack) - 1][1]
        else:
            return self.current_class_mem

    def next_mem_excluding_top(self):
        '''
        Similar to self.current_mem()) except the memory at the top of the stack is skipped.
        '''
        if len(self.fun_stack) > 1:
            return self.fun_stack[len(self.fun_stack) - 2][1]
        else:
            return self.current_class_mem

    def value(self, address):
        '''
        Returns the value of the given memory address that is stored in the currently active function memory, or global
        memory if there aren't any funs in the stack.
        '''
        if address in self.current_mem():
            return self.current_mem()[address]
        return self.current_class_mem[address]

    def value_excluding_top(self, address):
        '''
        Similar to self.value() except the memory a the top of the stack is skipped.
        '''
        if address in self.fun_stack[len(self.fun_stack) - 2][1]:
            return self.fun_stack[len(self.fun_stack) - 2][1][address]
        return self.current_class_mem[address]

    def execute(self):
        for sym_table in self.symbol_tables:
            memory = {}
            self.classes_memory[sym_table.cid] = memory
            globals = sym_table.get_global_table()
            for type in globals.keys():
                for key in globals[type]:
                    if type == 'bool':
                        if key == "True":
                            default_val = True
                        else:
                            default_val = False
                    elif type == 'int':
                        try:
                            default_val = int(key)
                        except ValueError:
                            default_val = 0
                    elif type == 'float':
                        try:
                            default_val = float(key)
                        except ValueError:
                            default_val = 0.0
                    elif type == 'string':
                        try:
                            default_val = str(key)
                        except ValueError:
                            default_val = ""
                    else:
                        default_val = None
                    memory[globals[type][key]] = default_val
            self.current_class_mem = memory

        print("Executing...")
        i = 0
        while i != len(self.quadruples):
            quad = self.quadruples[i]
            if quad[0] == 'GOTO':
                i = self.quadruples[i][3]
            elif quad[0] == 'GOTOF':
                if self.current_mem()[quad[1]]:
                    i += 1
                else:
                    i = self.quadruples[i][3]
            elif quad[0] == 'STARTPROC':
                i += 1
            elif quad[0] == 'ASG_PARAM':
                i += 1
                assignee = quad[3]
                # Pop the first value in the list of arguments from the stack's top 4-value tuple.
                value = self.fun_stack[len(self.fun_stack) - 1][2].pop(0)
                # Assign to the parameter var the value sent to the function.
                self.current_mem()[assignee] = self.value_excluding_top(value)
            elif quad[0] == 'ENDPROC':
                if len(self.fun_stack) > 0:
                    i, _, _, _ = self.fun_stack.pop()
                else:
                    i += 1
            elif quad[0] == 'ERA':
                # Adds a 4-value tuple to the stack. It will be later set to store:
                # 1. The index of the quadruples that we must jump to after executing the
                # function.
                # 2. The memory address/value map used to store local variables.
                # 3. A list of the memory addresses where the function arguments that are
                # being sent are stored.
                # 4. The temporary memory address that stores the result of the function
                # (if it has a return statement).
                self.fun_stack.append(['', {}, [], ''])
                i += 1
            elif quad[0] == 'param':
                i += 1
                # Add the address of this parameter to the list in the stacks' 4-value tuple.
                self.fun_stack[len(self.fun_stack) - 1][2].append(quad[1])
            elif quad[0] == 'GOSUB':
                # Set the index to jump to after executing the function.
                self.fun_stack[len(self.fun_stack) - 1][0] = i + 1
                # Save the address where we'll save the result of the function.
                self.fun_stack[len(self.fun_stack) - 1][3] = quad[2]
                i = quad[3]
            elif quad[0] == 'RETURN':
                i += 1
                value = quad[1]
                dest_address = self.fun_stack[len(self.fun_stack) - 1][3]
                if len(self.fun_stack) - 2 >= 0:
                    # If we're at least 2 levels deep then we set the result to the previous function's memory.
                    self.fun_stack[len(self.fun_stack) - 2][1][dest_address] = self.value(value)
                else:
                    # If we're only 1 level deep then we set the result to global memory.
                    self.current_class_mem[dest_address] = self.value(value)
            elif quad[0] == '=':
                value = quad[1]
                assignee = quad[3]
                self.current_mem()[assignee] = self.value(value)
                i += 1
            elif quad[0] in ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=']:
                if len(self.fun_stack) == 0:
                    self.current_class_mem[quad[3]] = operator_from_symbol(quad[0])(self.value(quad[1]), self.value(quad[2]))
                else:
                    # Check whether we should use the current memory (top of the stack or global) or the memory of the
                    # previous level. This is necessary because when evaluating quadruples inside a function a call such
                    # as 'a + b' in factorial(a + b)' we must save the result of 'a + b' in a temporary address of the
                    # scope in which it was called. Whoever, by the point in time when the parameters of the fun call
                    # are evaluated we have already processed the ERA operational code, which means that we have already
                    # appended a new tuple to the top of the fun stack. This means that when evaluating 'a + b', we must
                    # save its result not in the memory of the top of the fun stack, but in the memory of the tuple
                    # below that one, since that is the actual current scope (the tuple at the top of the stack will be
                    # come the 'current scope' until after executing the op code GOSUB, which comes after all the PARAM
                    # op codes).
                    if self.fun_stack[len(self.fun_stack) - 1][0] != '':
                        # If the first value of the fun stack's top tuple has been set, then we know we have already
                        # passed the GOSUB op code, so we must use the memory at the top of the stack.
                        self.current_mem()[quad[3]] = \
                            operator_from_symbol(quad[0])(self.value(quad[1]), self.value(quad[2]))
                    else:
                        # If the first value of the fun stack's top tuple has not been set, then we know we have not
                        # already passed the GOSUB op code, so we must use the memory below the top of the stack (as
                        # that holds the values of the current scope).
                        self.next_mem_excluding_top()[quad[3]] = \
                            operator_from_symbol(quad[0])(self.value_excluding_top(quad[1]),
                                                          self.value_excluding_top(quad[2]))
                i += 1
            elif quad[0] == 'WRITE':
                address = quad[1]
                if address != '':
                    value = self.value(address)
                    print(str(value), end='')
                else:
                    print()
                i += 1
            elif quad[0] == 'NEW_OBJ':
                cid = quad[1]
                assignee = quad[2]
                self.current_mem()[assignee] = copy.deepcopy(self.classes_memory[cid])
                self.obj_const_stack.append(['', [], assignee])
                i += 1
            elif quad[0] == 'OBJ_MEMBER':
                value_address = quad[1]
                self.obj_const_stack[len(self.obj_const_stack) - 1][1].append(value_address)
                i += 1
            elif quad[0] == 'ASG_MEMBER':
                member_dest_address = quad[3]
                next_quad, members, obj_address = self.obj_const_stack[len(self.obj_const_stack) - 1]
                self.current_mem()[obj_address][member_dest_address] = self.value(members.pop(0))
                if len(members) > 0:
                    i += 1
                else:
                    i = next_quad
            elif quad[0] == 'OBJ_CONST':
                self.obj_const_stack[len(self.obj_const_stack) - 1][0] = i + 1
                i = quad[3]
            elif quad[0] == 'START_CLASS':
                i += 1
            elif quad[0] == 'END_CLASS':
                i += 1
            elif quad[0] == 'GET_OBJ_MEM':
                obj_address = quad[1]
                member_address = quad[2]
                res_address = quad[3]
                self.current_mem()[res_address] = self.current_mem()[obj_address][member_address]
                i += 1
            else:
                raise Exception("Unexpected operation code: " + quad[0])
        print("Execution finished")
