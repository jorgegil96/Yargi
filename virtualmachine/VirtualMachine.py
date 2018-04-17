from typing import List
import operator
from util.utils import operator_from_symbol


class VirtualMachine:
    stack = []
    memory = {}

    def __init__(self, quadruples: List, globals: dict):
        self.quadruples = quadruples
        self.globals = globals

    def execute(self):
        for type in self.globals.keys():
            for key in self.globals[type]:
                default_val = None
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
                self.memory[self.globals[type][key]] = default_val

        print("Executing...")
        i = 0
        while i != len(self.quadruples):
            quad = self.quadruples[i]
            if quad[0] == 'GOTO':
                i = self.quadruples[i][3]
            elif quad[0] == 'GOTOF':
                if self.memory[quad[1]]:
                    i += 1
                else:
                    i = self.quadruples[i][3]
            elif quad[0] == 'STARTPROC':
                print("Start of fun " + quad[1])
                i += 1
            elif quad[0] == 'ENDPROC':
                print("End of fun " + quad[1])
                if len(self.stack) > 0:
                    i = self.stack.pop()
                else:
                    i += 1
            elif quad[0] == 'ERA':
                print("ERA for fun " + quad[1])
                i += 1
            elif quad[0] == 'param':
                print("Sending param " + quad[3] + " with address " + str(quad[1]))
                i += 1
            elif quad[0] == 'GOSUB':
                print("GOSUB for fun " + quad[1])
                self.stack.append(i + 1)
                i = quad[3]
            elif quad[0] == 'RETURN':
                print("RETURN")
                i += 1
            elif quad[0] == '=':
                print("ASSIGNMENT")
                value = quad[1]
                assignee = quad[3]
                self.memory[assignee] = self.memory[value]
                i += 1
            elif quad[0] == '+':
                print("SUM")
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '-':
                print("SUB")
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '*':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '/':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '>':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '<':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '>=':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '>=':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '==':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
            elif quad[0] == '!=':
                self.binary_op(quad[1], quad[2], quad[3], operator_from_symbol(quad[0]))
                i += 1
        print("Execution finished")
        for key in self.memory:
            print(str(key) + " => " + str(self.memory[key]))

    def binary_op(self, left, right, assignee, op: operator):
        self.memory[assignee] = op(self.memory[left], self.memory[right])
