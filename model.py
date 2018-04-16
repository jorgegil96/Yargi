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
        address, type = self.value.eval()  # address and type of the result.

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
        address = symbol_table.add_sym(str(self.varcte), cube_type, is_constant=True)
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


class TerminoR(BaseExpression):
    def __init__(self, optype, factor: BaseExpression, termino_r: BaseExpression):
        self.optype = optype  # POR or SOBRE
        self.factor = factor
        self.termino_r = termino_r

    def __repr__(self):
        return '<TerminoR optype={0} factor={1} termino_r={2}>'\
            .format(self.optype, self.factor, self.termino_r)

    def eval(self):
        if self.termino_r is None:
            return self.factor.eval()
        else:
            left_address, left_type = self.factor.eval()
            right_address, right_type = self.termino_r.eval()
            op_type = get_op_type_from_operator(self.termino_r.optype)

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class Termino(BaseExpression):
    def __init__(self, factor: BaseExpression, termino_r: TerminoR):
        self.factor = factor
        self.termino_r = termino_r

    def __repr__(self):
        return '<Termino factor={0} termino_r={1}>'.format(self.factor, self.termino_r)

    def eval(self):
        if self.termino_r is None:
            return self.factor.eval()
        else:
            left_address, left_type = self.factor.eval()
            right_address, right_type = self.termino_r.eval()
            op_type = get_op_type_from_operator(self.termino_r.optype)

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


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
    elif op == operator.mul:
        return '*'
    elif op == operator.floordiv:
        return '/'


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
            op_type = get_op_type_from_operator(self.exp_r.op)

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class RelationalOperand(BaseExpression):
    def __init__(self, type, exp: Exp):
        self.type = type
        self.exp = exp

    def __repr__(self):
        return '<RelationalOperand type={0} exp={1}>'.format(self.type, self.exp)

    def eval(self):
        return self.exp.eval()


class RelationalOperation(BaseExpression):
    def __init__(self, exp: Exp, relational_operand: RelationalOperand):
        self.exp = exp
        self.relational_operand = relational_operand

    def __repr__(self):
        return '<RelationalOperation exp={0} relational_operand={1}>' \
            .format(self.exp, self.relational_operand)

    def eval(self):
        if self.relational_operand is None:
            return self.exp.eval()
        else:
            left_address, left_type = self.exp.eval()
            right_address, right_type = self.relational_operand.eval()
            op_type = self.relational_operand.type

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class LogicalOperand(BaseExpression):
    def __init__(self, type, super_exp: RelationalOperation, logical_operand: BaseExpression):
        self.type = type
        self.super_exp = super_exp
        self.logical_operand = logical_operand

    def __repr__(self):
        return '<LogicalOperand type={0} super_exp={1} logical_operand={2}>'\
            .format(self.type, self.super_exp, self.logical_operand)

    def eval(self):
        if self.logical_operand is None:
            return self.super_exp.eval()
        else:
            left_address, left_type = self.super_exp.eval()
            right_address, right_type = self.logical_operand.eval()
            op_type = get_op_type_from_operator(self.logical_operand.type)

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class LogicalOperation(BaseExpression):
    def __init__(self, super_exp: RelationalOperation, logical_operand: LogicalOperand):
        self.super_exp = super_exp
        self.logical_operand = logical_operand

    def __repr__(self):
        return '<LogicalOperation rel_operation={0} logical_operand={1}>' \
            .format(self.super_exp, self.logical_operand)

    def eval(self):
        if self.logical_operand is None:
            return self.super_exp.eval()
        else:
            left_address, left_type = self.super_exp.eval()
            right_address, right_type = self.logical_operand.eval()
            op_type = self.logical_operand.type

            res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = symbol_table.add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class If(BaseExpression):
    def __init__(self, base_exp: BaseExpression, true_stmts: List[BaseExpression], false_stmts: List[BaseExpression]):
        self.base_exp = base_exp
        self.true_stmts = true_stmts
        self.false_stmts = false_stmts

    def __repr__(self):
        return '<If base_exp={0} true_stms={1}>'\
            .format(self.base_exp, self.true_stmts)

    def eval(self):
        exp_address, exp_type = self.base_exp.eval()
        if exp_type != 'bool':
            raise Exception("Conditional statement must evaluate to bool")

        gotof = ['GOTOF', exp_address, '', '']
        quadruples.append(gotof)

        # Generate quadruples for the true statements.
        for stmt in self.true_stmts:
            stmt.eval()

        goto = ['GOTO', '', '', '']
        quadruples.append(goto)

        # Set the jump address of the gotof to after the goto quadruple.
        gotof[3] = len(quadruples)

        # Generate quadruples for the false statements.
        for stmt in self.false_stmts:
            stmt.eval()

        # Set the jump address of the goto to after the last false stmt quadruple.
        goto[3] = len(quadruples)


class Range(BaseExpression):
    def __init__(self, start: ConstantVar, end: ConstantVar):
        self.start = start
        self.end = end

    def __repr__(self):
        return '<Range start={0} end={1}>'.format(self.start, self.end)

    def eval(self):
        start_address, start_type = self.start.eval()
        end_address, end_type = self.end.eval()

        if start_type != 'int' or end_type != 'int':
            raise Exception("Range arguments must be of type int")

        return start_address, start_type, end_address, end_type


class ForIn(BaseExpression):
    def __init__(self, id, range: Range, stmts: List[BaseExpression]):
        self.id = id
        self.range = range
        self.stmts = stmts

    def __repr__(self):
        return '<ForIn id={0} range={1} stmts={2}>'.format(self.id, self.range, self.stmts)

    def eval(self):
        # Create constant '1' in case it doesn't exist since it will be used to + 1 the counter.
        ConstantVar(1, 'INTNUM').eval()
        one_const_address, one_const_type = symbol_table.get_sym_address_and_type('1')

        start_address, start_type, end_address, end_type = self.range.eval()
        id_address, id_type = symbol_table.get_sym_address_and_type(self.id)

        if id_type != 'int':
            raise Exception("For iterable must be of type int")

        # Create quadruple to assign the start address to the id address.
        # e.g. in "for(x in a..b)", x is assigned the value of a.
        quadruples.append(['=', start_address, '', id_address])

        # Verify that result of x < b is bool.
        op_type = '<'
        res_type = cube[id_type][end_type][op_type]
        if res_type != 'bool':
            raise Exception("Illegal state: result type should be of type bool")

        # Add register for temp result.
        address = symbol_table.add_temp(res_type)
        # Create quadruple for the "x < b" operation.
        quadruples.append([op_type, id_address, end_address, address])

        # Save the index of the condition quadruple.
        cond_index = len(quadruples) - 1

        gotof = ["GOTOF", address, '', '']
        quadruples.append(gotof)

        # Add quadruples for each statement.
        for stmt in self.stmts:
            stmt.eval()

        # Generate quadruple for temp = x + 1.
        res_type_2 = cube[id_type][one_const_type]['+']
        address = symbol_table.add_temp(res_type_2)
        quadruples.append(['+', id_address, one_const_address, address])

        # Generate quadruple for x = temp.
        quadruples.append(['=', address, '', id_address])

        # Generate goto to return to the condition quadruple.
        quadruples.append(["GOTO", '', '', cond_index])

        # We reached the end of the for quadruples, point the gotof to the next one.
        gotof[3] = len(quadruples)


class While(BaseExpression):
    def __init__(self, base_exp: BaseExpression, stmts: List[BaseExpression]):
        self.base_exp = base_exp
        self.stmts = stmts

    def __repr__(self):
        return '<While base_exp={0} stmts={1}>'.format(self.base_exp, self.stmts)

    def eval(self):
        cond_index = len(quadruples)
        exp_address, exp_type = self.base_exp.eval()
        if exp_type != 'bool':
            raise Exception("While statement must evaluate to bool")

        gotof = ["GOTOF", exp_address, '', '']
        quadruples.append(gotof)

        for stmt in self.stmts:
            stmt.eval()

        goto = ["GOTO", '', '', cond_index]
        quadruples.append(goto)

        gotof[3] = len(quadruples)
