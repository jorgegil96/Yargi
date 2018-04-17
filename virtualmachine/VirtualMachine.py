from typing import List
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
                i += 1
            elif quad[0] == 'ENDPROC':
                if len(self.stack) > 0:
                    i = self.stack.pop()
                else:
                    i += 1
            elif quad[0] == 'ERA':
                i += 1
            elif quad[0] == 'param':
                i += 1
            elif quad[0] == 'GOSUB':
                self.stack.append(i + 1)
                i = quad[3]
            elif quad[0] == 'RETURN':
                i += 1
            elif quad[0] == '=':
                value = quad[1]
                assignee = quad[3]
                self.memory[assignee] = self.memory[value]
                i += 1
            elif quad[0] in ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=']:
                self.memory[quad[3]] = operator_from_symbol(quad[0])(self.memory[quad[1]], self.memory[quad[2]])
                i += 1
        print("Execution finished")
        for key in self.memory:
            print(str(key) + " => " + str(self.memory[key]))
