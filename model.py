class VarDeclaration:
    def __init__(self, name, type, visibility):
        self.name = name
        self.type = type
        if visibility is None:
            self.visibility = "public"
        else:
            self.visibility = visibility

    def __str__(self):
        return "var %s of type %s with %s visibility\n" % (self.name, self.type, self.visibility)


class Fun:
    def __init__(self, name, type, visibility, body):
        self.name = name
        self.type = type
        self.visibility = visibility
        self.body = body

    def __str__(self):
        s = "function %s with %s visibility returns %s and has %s local vars\n" % (
            self.name, self.visibility, self.type, len(self.body.vars))
        s += "          Local vars:\n"
        if len(self.body.vars) == 0:
            s += "              No local vars...\n"
        else:
            for var in self.body.vars:
                s += "              " + str(var)
        return s


class FunBody:
    def __init__(self, vars, statements):
        self.vars = vars
        self.statements = statements


class Class:
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __str__(self):
        s = "Class %s contains %s global vars and %s functions:\n" % (
            self.name, len(self.body.vars), len(self.body.funs))
        s += "  Global vars:\n"
        if len(self.body.vars) == 0:
            s += "      No global vars...\n"
        else:
            for var in self.body.vars:
                s += "      " + str(var)
        s += "  Functions:\n"
        if len(self.body.funs) == 0:
            s += "      No functions...\n"
        else:
            for fun in self.body.funs:
                s += "      " + str(fun)
        return s


class ClassBody:
    def __init__(self, vars, funs):
        self.vars = vars
        self.funs = funs


class Assignment:
    def __init__(self, id, value):
        self.id = id
        self.value = value
