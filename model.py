from typing import List
from semantics.semantic_analyser import SymbolTable
import operator
from semantic_cube import cube
from util import utils

symbol_table = SymbolTable()
quadruples = []


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
        symbol_table.add_sym(self.name, self.type)


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
        address, type = self.value.eval() # address and type of the result.

        # Verify that the variable to assign to exists and is of correct type. Throws if invalid.
        symbol_table.verify_sym_declared_with_correct_type(self.id, utils.parser_type_to_cube_type(type))

        assignee_address, assignee_type = symbol_table.get_sym_address_and_type(self.id)

        quadruples.append(['=', address, '', assignee_address])


class ConstantVar(BaseExpression):
    def __init__(self, varcte, type):
        self.varcte = varcte
        self.type = type

    def __repr__(self):
        return '<ConstantVar varcte={0} type={1}>'.format(self.varcte, self.type)

    def eval(self):
        if self.type == "ID":
            return symbol_table.get_sym_address_and_type(self.varcte)

        # Varcte if a primitive
        cube_type = utils.parser_type_to_cube_type(self.type)

        # Add constant primititive to symbol table with its a value as its name.
        # e.g. for varcte = 5 of type INTNUM, call add_sym('5', 'int').
        # This creates a record(memory address) in the symbol table for the constant 5 indexed as '5'.
        address = symbol_table.add_sym(str(self.varcte), cube_type)
        return address, cube_type


class ArithmeticOperand(BaseExpression):
    """
    E.g. + 5, - x
    """

    def __init__(self, op: operator, varcte: BaseExpression):
        self.op = op
        self.varcte = varcte

    def __repr__(self):
        return '<ArithmeticOperand operator={0} varcte={1}>'.format(self.op, self.varcte)

    def eval(self):
        return self.varcte.eval()


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


class ExpR(BaseExpression):
    def __init__(self, op: operator, termino: Termino, exp_r: BaseExpression):
        self.op = op
        self.termino = termino
        self.exp_r = exp_r

    def __repr__(self):
        return '<ExpR op={0} termino={1} exp_r={2}>' \
            .format(self.op, self.termino, self.exp_r)

    def eval(self):
        if self.exp_r is None:
            return self.termino.eval()
        else:
            left_address, left_type = self.termino.eval()
            right_address, right_type = self.exp_r.eval()
            opType = get_op_type_from_operator(self.exp_r.op)

            res_type = cube[left_type][right_type][opType]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(opType, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([opType, left_address, right_address, address])
            return address, res_type


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
            left_address, left_type = self.termino.eval()
            right_address, right_type = self.exp_r.eval()
            opType = get_op_type_from_operator(self.exp_r.op)

            res_type = cube[left_type][right_type][opType]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(opType, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([opType, left_address, right_address, address])
            return address, res_type


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
