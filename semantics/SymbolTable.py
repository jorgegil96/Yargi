from model import *

SCOPE_GLOBAL = "GLOBAL"
SCOPE_LOCAL = "LOCAL"


class SymbolTable:
    # Stores the functions of the program
    __fun_dir = {}
    # Stores the variable table of the global scope
    __global_sym_table = {}
    # Stores a list a variable tables of local scope
    __local_sym_tables = []

    def __repr__(self):
        return '<SymbolTable\n fun_dir={0}\n global_sym_table={1}\n local_sym_tables={2}>' \
            .format(self.__fun_dir, self.__global_sym_table, self.__local_sym_tables)

    def get_current_scope(self):
        '''
        Returns SCOPE_GLOBAL if there are no local sym tables, true otherwise.
        '''
        if len(self.__local_sym_tables) > 0:
            return SCOPE_LOCAL
        else:
            return SCOPE_GLOBAL

    def get_local_table(self):
        '''
        :return: the current local table, i.e. the one on top of the stack.
        '''
        return self.__local_sym_tables[len(self.__local_sym_tables) - 1]

    def set_scope(self, scope):
        if scope == SCOPE_LOCAL:
            self.__local_sym_tables.append({})
        else:
            self.__local_sym_tables.pop()

    def add_fun(self, fun):
        '''
        Adds a function to the fun directory.
        Throws an exception if a function under that name already exists.
        '''
        if fun.name in self.__fun_dir:
            raise Exception("Function %s is already declared" % fun.name)

        self.__fun_dir[fun.name] = fun

    def add_sym(self, var):
        '''
        Adds a symbol to the current local active table, or the global table if
        there aren't any locals.
        '''
        if self.get_current_scope() == SCOPE_LOCAL:
            self.get_local_table()[var.name] = var
        else:
            self.__global_sym_table[var.name] = var

    def set_sym_value(self, id, value):
        '''
        Sets the given value to the specified id.
        The id must already be declared.
        '''
        if self.get_current_scope() == SCOPE_LOCAL:
            if id in self.get_local_table():
                self.get_local_table()[id] = value
                return

        if id in self.__global_sym_table:
            self.__global_sym_table[id] = value
            return

        raise Exception("Assignment of undeclared variable %s of value %s" % id, value)

    def get_sym_value(self, id):
        if self.get_current_scope() == SCOPE_LOCAL:
            if id in self.get_local_table():
                return self.get_local_table()[id]

        return self.__global_sym_table[id]

    def is_sym_declared(self, id):
        '''
        Returns true if the given id is declared in a valid scope, i.e. the current
        local function or the global scope.
        '''
        if self.get_current_scope() == SCOPE_GLOBAL:
            return id in self.__global_sym_table
        else:
            return id in self.__global_sym_table or id in self.get_local_table()
