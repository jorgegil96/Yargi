SCOPE_GLOBAL = "GLOBAL"
SCOPE_LOCAL = "LOCAL"


class SymbolTable:
    # Stores the functions of the program
    __fun_dir = {}
    # Stores the variable table of the global scope
    __global_sym_table = {}
    # Stores a list a variable tables of local scope
    __local_sym_tables = []
    # Stores the variable table for temporary vars
    __temp_sym_table = {}

    __temp_counter = 0

    __int_pointer = 0
    __float_pointer = 5000
    __bool_pointer = 10000
    __string_pointer = 15000
    __last_pointer = 0

    def __repr__(self):
        return '<SymbolTable\n fun_dir={0}\n global_sym_table={1}\n local_sym_tables={2}>' \
            .format(self.__fun_dir, self.__global_sym_table, self.__local_sym_tables)

    def get_global_table(self):
        return self.__global_sym_table

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
            print("LOCAL TABLE START")
            print(self.get_local_table())
            print("LOCAL TABLE END")
            self.__local_sym_tables.pop()

    def add_fun(self, fun):
        '''
        Adds a function to the fun directory.
        Throws an exception if a function under that name already exists.
        '''
        if fun.name in self.__fun_dir:
            raise Exception("Function %s is already declared" % fun.name)

        self.__fun_dir[fun.name] = fun

    def get_fun(self, fun_name):
        if fun_name in self.__fun_dir:
            return self.__fun_dir[fun_name]

        raise Exception("Function %s not found" % fun_name)

    def add_sym(self, name, type, is_constant=False):
        '''
        Adds a symbol to the current local active table, or the global table if
        there aren't any locals.
        '''
        if is_constant:
            table = self.__global_sym_table
        else:
            if name == "temp":
                table = self.__temp_sym_table
            else:
                if self.get_current_scope() == SCOPE_LOCAL:
                    table = self.get_local_table()
                else:
                    table = self.__global_sym_table

        if name in table:
            raise Exception("Var %s is already declared" % name)

        # Create inner table for types in current table
        if type not in table:
            table[type] = {}

        if name == "temp":
            name = "t" + str(self.__temp_counter)
            self.__temp_counter += 1

        if name in table[type]:
            return table[type][name]
        if type == "int":
            table[type][name] = self.__int_pointer
            self.__last_pointer = self.__int_pointer
            self.__int_pointer += 1
        elif type == "float":
            table[type][name] = self.__float_pointer
            self.__last_pointer = self.__float_pointer
            self.__float_pointer += 1
        elif type == "bool":
            table[type][name] = self.__bool_pointer
            self.__last_pointer = self.__bool_pointer
            self.__bool_pointer += 1
        elif type == "string":
            table[type][name] = self.__string_pointer
            self.__last_pointer = self.__string_pointer
            self.__string_pointer += 1
        else:
            raise Exception("Invalid type %s" % type)
        return self.__last_pointer

    def add_temp(self, type):
        '''
        Adds a temporary symbol to the current active table.
        '''
        return self.add_sym("temp", type)

    def verify_sym_declared_with_correct_type(self, id, type):
        '''
        Verifies that the given symbol is declared in the appropriate scope and that its type matches the given type.
        Throws if verification fails.
        '''
        if self.get_current_scope() == SCOPE_GLOBAL:
            declared = False
            for type_table in self.__global_sym_table.keys():
                if id in self.__global_sym_table[type_table]:
                    declared = True

            if not declared:
                raise Exception("Use of undefined variable %s" % id)

            if id not in self.__global_sym_table[type]:
                raise Exception("Assignment of type %s to var of different type" % type)
        else:
            declared = False
            for type_table in self.__global_sym_table.keys():
                if id in self.__global_sym_table[type_table]:
                    declared = True

            for type_table in self.get_local_table().keys():
                if id in self.get_local_table()[type_table]:
                    declared = True

            if not declared:
                raise Exception("Use of undefined variable %s" % id)

        found = False
        local_table = self.get_local_table()
        if type in local_table and id in local_table[type]:
            found = True
        if type in self.__global_sym_table and id in self.__global_sym_table[type]:
            found = True

        if not found:
            raise Exception("Assignment of type %s to var of different type" % type)

    def get_sym_address_and_type(self, name):
        '''
        Given the name of the symbol, returns the address where it is stored and its type.
        Throws if it doesn't exist.
        '''
        if self.get_current_scope() == SCOPE_LOCAL:
            for key in self.get_local_table().keys():
                for id in self.get_local_table()[key]:
                    if id == name:
                        return self.get_local_table()[key][id], key

        for key in self.__global_sym_table.keys():
            for id in self.__global_sym_table[key]:
                if id == name:
                    return self.__global_sym_table[key][id], key

        raise Exception("Variable %s does not exist" % name)
