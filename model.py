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


class ConstantVar:
    def __init__(self, varcte):
        self.varcte = varcte


class ArithmeticOperand:
    """
    E.g. + 5, - x
    """
    def __init__(self, type, varcte):
        self.type = type
        self.varcte = varcte


class TerminoR:
    def __init__(self, optype2, factor, termino_r):
        self.optype2 = optype2
        self.factor = factor
        self.termino_r = termino_r


class Termino:
    def __init__(self, factor, termino_r: TerminoR):
        self.factor = factor
        self.termino_r = termino_r


class ExpR:
    def __init__(self, optype, termino: Termino, exp_r):
        self.optype = optype
        self.termino = termino
        self.exp_r = exp_r


class Exp:
    def __init__(self, termino: Termino, exp_r: ExpR):
        self.termino = termino
        self.exp_r = exp_r


class RelationalOperand:
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp


class RelationalOperation:
    def __init__(self, exp: Exp, relational_operand: RelationalOperand):
        self.exp = exp
        self.relational_operand = relational_operand


class LogicalOperand:
    def __init__(self, type, super_exp, logical_operand):
        self.type = type
        self.super_exp = super_exp
        self.logical_operand = logical_operand


class LogicalOperation:
    def __init__(self, super_exp: RelationalOperation, logical_operand: LogicalOperand):
        self.super_exp = super_exp
        self.logical_operand = logical_operand
