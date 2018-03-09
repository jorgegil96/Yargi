class FunDirectory:
    def __init__(self):
        self.fun_entries = {}
        self.active_fun = None

    def add_entry(self, entry):
        self.fun_entries[entry.name] = entry

    def add_var_to_active_fun(self, name, var_type):
        self.fun_entries[self.active_fun].var_table.add_var(name, var_type)

    def get_active(self):
        return self.active_fun

    def set_active(self, name):
        self.active_fun = name

    def print(self):
        for fun_name, entry in self.fun_entries:
            print(fun_name + " returns type " + entry.var_type + " has vars:")
            for var_name, var_type in entry.var_table.vars:
                print(var_name + "is of type " + var_type)
