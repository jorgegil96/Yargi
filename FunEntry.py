from VarTable import *


class FunEntry:
    def __init__(self, name, var_type):
        self.name = name
        self.var_type = var_type
        self.var_table = VarTable()
