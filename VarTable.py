class VarTable:
    def __init__(self):
        self.vars = {}

    def add_var(self, name, var_type):
        self.vars[name] = var_type
