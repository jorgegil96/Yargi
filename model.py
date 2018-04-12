from typing import List
from semantics.semantic_analyser import SymbolTable
import operator
from semantic_cube import cube

symbol_table = SymbolTable()


class BaseExpression:
    def eval(self):
        raise Exception("eval() not implemented")


class VarDeclaration(BaseExpression):
    def __init__(self, name, type, visibility):
        self.name = name
        self.type = type
        if visibility is None:
            self.visibility = "public"
        else:
            self.visibility = visibility
        self.value = 0

    def __repr__(self):
        return '<VarDeclaration name={0} type={1} visibility={2} value={3}>' \
            .format(self.name, self.type, self.visibility, self.value)

    def eval(self):
        symbol_table.add_sym(self)


class FunBody(BaseExpression):
    def __init__(self, vars: List[VarDeclaration], statements: List[BaseExpression]):
        self.vars = vars
        self.statements = statements

    def __repr__(self):
        return '<FunBody vars_len={0} stmts_len={1} vars={2} statements={3}>' \
            .format(len(self.vars), len(self.statements), self.vars, self.statements)

    def eval(self):
        for var in self.vars:
            var.eval()
        for stmt in self.statements:
            stmt.eval()


class Fun(BaseExpression):
    def __init__(self, name, type, visibility, body: FunBody):
        self.name = name
        self.type = type
        self.visibility = visibility
        self.body = body

    def __repr__(self):
        return '<Fun name={0} type={1} visibility={2} body={3}>' \
            .format(self.name, self.type, self.visibility, self.body)

    def eval(self):
        symbol_table.add_fun(self)
        symbol_table.set_scope("LOCAL")
        self.body.eval()
        symbol_table.set_scope("GLOBAL")


class ClassBody(BaseExpression):
    def __init__(self, vars: List[VarDeclaration], funs: List[Fun]):
        self.vars = vars
        self.funs = funs

    def __repr__(self):
        return '<ClassBody vars_len={0} funs_len={1} vars={2} funs={3}>' \
            .format(len(self.vars), len(self.funs), self.vars, self.funs)

    def eval(self):
        for var in self.vars:
            var.eval()
        for fun in self.funs:
            fun.eval()


class Class(BaseExpression):
    def __init__(self, name, body: ClassBody):
        self.name = name
        self.body = body

    def __repr__(self):
        return '<Class name={0} body={1}>'.format(self.name, self.body)

    def eval(self):
        self.body.eval()


class Assignment(BaseExpression):
    def __init__(self, id, value: BaseExpression):
        self.id = id
        self.value = value

    def __repr__(self):
        return '<Assignment id={0} value={1}>'.format(self.id, self.value)

    def eval(self):
        # Verify that the variable to assign to exists.
        if not symbol_table.is_sym_declared(self.id):
            raise Exception("Use of undefined variable %s" % self.id)

        symbol_table.set_sym_value(self.id, self.value.eval())


class ConstantVar(BaseExpression):
    def __init__(self, varcte, type):
        self.varcte = varcte
        self.type = type

    def __repr__(self):
        return '<ConstantVar varcte={0} type={1}>'.format(self.varcte, self.type)

    def eval(self):
        if self.type == "ID":
            return symbol_table.get_sym_value(self.varcte)
        return self.varcte


class ArithmeticOperand(BaseExpression):
    """
    E.g. + 5, - x
    """

    def __init__(self, op: operator, varcte):
        self.op = op
        self.varcte = varcte

    def __repr__(self):
        return '<ArithmeticOperand operator={0} varcte={1}>'.format(self.op, self.varcte)

    def eval(self):
        return self


class TerminoR:
    def __init__(self, optype2, factor, termino_r):
        self.optype2 = optype2
        self.factor = factor
        self.termino_r = termino_r


class Termino(BaseExpression):
    def __init__(self, factor: BaseExpression, termino_r: TerminoR):
        self.factor = factor
        self.termino_r = termino_r

    def __repr__(self):
        return '<Termino factor={0} termino_r={1}>'.format(self.factor, self.termino_r)

    def eval(self):
        return self.factor.eval()
        '''
        if isinstance(self.factor, ConstantVar):
            self.factor.eval()
        elif isinstance(self.factor, ArithmeticOperand):
        '''


class ExpR(BaseExpression):
    def __init__(self, op: operator, termino: Termino, exp_r: BaseExpression):
        self.op = op
        self.termino = termino
        self.exp_r = exp_r

    def __repr__(self):
        return '<ExpR op={0} termino={1} exp_r={2}>' \
            .format(self.op, self.termino, self.exp_r)

    def eval(self):
        self.termino.eval()
        self.exp_r.eval()


def get_type_from_instance(value):
    if isinstance(value, bool):
        return 'bool'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'float'


def get_op_type_from_operator(op: operator):
    if op == operator.add:
        return '+'
    elif op == operator.sub:
        return '-'


class Exp(BaseExpression):
    def __init__(self, termino: Termino, exp_r: ExpR):
        self.termino = termino
        self.exp_r = exp_r

    def __repr__(self):
        return '<Exp termino={0} exp_r={1}>'.format(self.termino, self.exp_r)

    def eval(self):
        if self.exp_r is None:
            return self.termino.eval()
        else:
            left = self.termino.eval()
            right = self.exp_r.termino.eval()

            leftType = get_type_from_instance(left)
            rightType = get_type_from_instance(right)
            opType = get_op_type_from_operator(self.exp_r.op)

            res = cube[leftType][rightType][opType]
            if res is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(opType, leftType, rightType))

            result = self.exp_r.op(left, right)
            return result


class RelationalOperand:
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp


class RelationalOperation(BaseExpression):
    def __init__(self, exp: Exp, relational_operand: RelationalOperand):
        self.exp = exp
        self.relational_operand = relational_operand

    def __repr__(self):
        return '<RelationalOperation exp={0} relational_operand={1}>' \
            .format(self.exp, self.relational_operand)

    def eval(self):
        return self.exp.eval()


class LogicalOperand:
    def __init__(self, type, super_exp, logical_operand):
        self.type = type
        self.super_exp = super_exp
        self.logical_operand = logical_operand


class LogicalOperation(BaseExpression):
    def __init__(self, super_exp: RelationalOperation, logical_operand: LogicalOperand):
        self.super_exp = super_exp
        self.logical_operand = logical_operand

    def __repr__(self):
        return '<LogicalOperation rel_operation={0} logical_operand={1}>' \
            .format(self.super_exp, self.logical_operand)

    def eval(self):
        return self.super_exp.eval()
