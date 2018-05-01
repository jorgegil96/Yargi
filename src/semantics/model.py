import operator
from typing import List

from src.semantics.SemanticCube import cube
from src.semantics.SymbolTable import SymbolTable
from src.util import utils

# Each element in the list stores the SymbolTable for a class.
symbol_tables = []

# Once a class is parsed (poped from the 'symbol_tables' stack it is stored here for
# future use.
final_sym_tables: List[SymbolTable] = []

quadruples = []


def last_symbol_table():
    '''
    Returns the symbol table at the top of the stack without poping it.
    '''
    return symbol_tables[len(symbol_tables) - 1]


def symbol_table_for_type(type):
    for sym_table in final_sym_tables:
        if sym_table.cid == type:
            return sym_table


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
        return last_symbol_table().add_sym(self.name, self.type)


class Main(BaseExpression):
    def __init__(self, vars: List[VarDeclaration], stmts: List[BaseExpression]):
        self.name = 'main'
        self.vars = vars
        self.stmts = stmts

    def __repr__(self):
        return '<Main vars={0} stmts={1}>'.format(self.vars, self.stmts)

    def eval(self):
        quadruples.append(['STARTPROC', self.name, '', ''])
        last_symbol_table().add_fun(self)
        last_symbol_table().set_scope("LOCAL")

        for var in self.vars:
            var.eval()
        for stmt in self.stmts:
            stmt.eval()

        last_symbol_table().set_scope("GLOBAL")

        quadruples.append(['ENDPROC', self.name, '', ''])


class FunBody(BaseExpression):
    def __init__(self, params: List[VarDeclaration], vars: List[VarDeclaration],
                 statements: List[BaseExpression], return_exp: BaseExpression):
        self.params = params
        self.vars = vars
        self.statements = statements
        self.return_exp = return_exp

    def __repr__(self):
        return '<FunBody num_params={0} params={1} vars_len={2} stmts_len={3} vars={4} statements={5} return_exp={6}>' \
            .format(len(self.params), self.params, len(self.vars), len(self.statements), self.vars, self.statements,
                    self.return_exp)

    def eval(self):
        for param in self.params:
            address = param.eval()
            quadruples.append(['ASG_PARAM', '', '', address])
        for var in self.vars:
            var.eval()
        for stmt in self.statements:
            stmt.eval()
        if self.return_exp is not None:
            ret_address, ret_type = self.return_exp.eval()
            quadruples.append(['RETURN', ret_address, ret_type, ''])


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
        quadruples.append(['STARTPROC', self.name, '', ''])
        last_symbol_table().add_fun(self)
        last_symbol_table().set_scope("LOCAL")
        self.body.eval()
        last_symbol_table().set_scope("GLOBAL")

        last_quad = quadruples[len(quadruples) - 1]
        if self.type != 'void':
            if last_quad[0] != 'RETURN':
                raise Exception("Missing return statement in fun %s" % self.name)
            if last_quad[2] != self.type:
                raise Exception("Return value must be of type {0} in fun {1} but was {2}"
                                .format(self.type, self.name, last_quad[2]))

        quadruples.append(['ENDPROC', self.name, '', ''])


class FunCall(BaseExpression):
    def __init__(self, fun_name, params: List[BaseExpression], of_object=None):
        self.fun_name = fun_name
        self.params = params
        self.of_object = of_object

    def __repr__(self):
        return '<FunCall fun_name={0} params={1}>'.format(self.fun_name, self.params)

    def eval(self):
        # The symbol table to be used depends on how the fun call was made.
        # If it was a normal 'foo()' call, i.e. a function of the class we're in then we must use the symbol table of
        # the current class, whoever, if the call was of the form 'object.foo()' then we must use the symbol table of
        # the instance of the class of that object.
        if self.of_object is not None:
            obj_address, obj_type = last_symbol_table().get_sym_address_and_type(self.of_object)
            symbol_table = symbol_table_for_type(obj_type)
        else:
            obj_type = last_symbol_table().cid
            obj_address = None
            symbol_table = last_symbol_table()

        fun: Fun = symbol_table.get_fun(self.fun_name)

        quadruples.append(["ERA", self.fun_name, obj_type, obj_address])

        if len(fun.body.params) != len(self.params):
            raise Exception("Fun {0} expected {1} arguments but was {2}"
                            .format(self.fun_name, len(fun.body.params), len(self.params)))

        for param_index in range(0, len(self.params)):
            fun_param = fun.body.params[param_index]
            call_param = self.params[param_index]

            address, type = call_param.eval()
            if type != fun_param.type:
                raise Exception("Expected {0} argument in function {1} call but was {2}"
                                .format(fun_param.type, self.fun_name, type))

            quadruples.append(['param', address, '', 'param' + str(param_index)])
            param_index += 1

        fun_start_quad_index = None
        curr_class = None
        for i in range(0, len(quadruples)):
            quad = quadruples[i]
            if quad[0] == 'START_CLASS':
                # Save the class type we're currently at for later use...
                curr_class = quad[1]
            if quad[0] == 'STARTPROC' and quad[1] == self.fun_name and curr_class == obj_type:
                if curr_class == obj_type:
                    fun_start_quad_index = i
                    break

        if fun_start_quad_index is None:
            raise Exception("Use of undefined function %s" % self.fun_name)

        if fun.type != 'void':
            address = last_symbol_table().add_temp(fun.type)
        else:
            address = ''

        quadruples.append(['GOSUB', self.fun_name, address, fun_start_quad_index])
        return address, fun.type


class ClassParent(BaseExpression):
    def __init__(self, name, params: List):
        self.name = name
        self.params = params


class ClassBody(BaseExpression):
    def __init__(self, vars: List[VarDeclaration], funs: List[Fun], main: Main):
        self.vars = vars
        self.funs = funs
        self.main = main

    def __repr__(self):
        return '<ClassBody vars_len={0} funs_len={1} vars={2} funs={3}>' \
            .format(len(self.vars), len(self.funs), self.vars, self.funs)

    def eval(self):
        for var in self.vars:
            var.eval()
        for fun in self.funs:
            fun.eval()
        if self.main is not None:
            quadruples[0][3] = len(quadruples)
            self.main.eval()


class Class(BaseExpression):
    def __init__(self, name, members: List[VarDeclaration], body: ClassBody, class_parent: ClassParent):
        self.name = name
        self.members = members
        self.body = body
        self.class_parent = class_parent

    def __repr__(self):
        return '<Class name={0} members={1} body={2}>'.format(self.name, self.members, self.body)

    def eval(self):
        symbol_tables.append(SymbolTable(self.name, self, 65000 * (len(symbol_tables))))
        quadruples.append(['START_CLASS', self.name, '', ''])
        for member in self.members:
            address = member.eval()
            quadruples.append(['ASG_MEMBER', '', '', address])

        if self.body is not None:
            self.body.eval()

        if self.class_parent is not None:
            # If we're extending a class...

            # Find the parent's symbol table.
            parent_sym_table = None
            for table in final_sym_tables:
                if table.cid == self.class_parent.name:
                    parent_sym_table = table

            if parent_sym_table is None:
                raise Exception("Invalid class name {0}".format(self.class_parent.name))

            # Verify that the length of the parent constructor call is equal to its signature.
            if len(parent_sym_table.class_model.members) != len(self.class_parent.params):
                raise Exception("{0} constructor expected {1} arguments".format(self.class_parent.name, len(
                    parent_sym_table.class_model.members)))

            # Verify that the call to the parent constructor has types that match.
            # E.g. for a class declaration "class Student(int id, string name): Person(id, name)"
            # we verify that the first argument of Person(int id, string name) is and int and the second
            # a string.
            for i in range(0, len(parent_sym_table.class_model.members)):
                expected_type = parent_sym_table.class_model.members[i].type
                sent_param_id = self.class_parent.params[i]
                actual_type = None
                for member in self.members:
                    if member.name == sent_param_id:
                        actual_type = member.type

                if actual_type is None:
                    raise Exception("Invalid argument {0} at pos({1})".format(sent_param_id, i))

                if expected_type != actual_type:
                    raise Exception("{0} constructor expected {1} at pos({2}) but was {3}"
                                    .format(self.class_parent.name, expected_type, i, actual_type))

            fun_dir = parent_sym_table.get_fun_dir()
            for fun_name in fun_dir.keys():
                if fun_name not in last_symbol_table().get_fun_dir():
                    # Eval every fun in the superclass to generate quadruples for that fun inside this class.
                    fun_dir[fun_name].eval()
                else:
                    # If it was already in the symbol table then it means we overrode it.
                    # Verify its arguments have the same signature.
                    parent_fun_params = fun_dir[fun_name].body.params
                    child_fun_params = last_symbol_table().get_fun(fun_name).body.params

                    if len(parent_fun_params) != len(child_fun_params):
                        raise Exception("Fun {0} is already defined".format(fun_name))

                    for i in range(0, len(parent_fun_params)):
                        parent_param = parent_fun_params[i]
                        child_param = child_fun_params[i]
                        if parent_param.type != child_param.type:
                            raise Exception("Overriden fun {0} expected {1} argument at pos({2}) but was {3}"
                                            .format(fun_name, parent_param.type, i, child_param.type))

        quadruples.append(['END_CLASS', self.name, '', ''])
        table: SymbolTable = symbol_tables.pop()
        final_sym_tables.append(table)


class Assignment(BaseExpression):
    def __init__(self, id, value: BaseExpression):
        self.id = id
        self.value = value

    def __repr__(self):
        return '<Assignment id={0} value={1}>'.format(self.id, self.value)

    def eval(self):
        if isinstance(self.value, Read):
            input = self.value.eval()
            assignee_address, assignee_type = last_symbol_table().get_sym_address_and_type(self.id)

            if assignee_type == 'bool':
                if input == "true":
                    val = True
                elif input == "false":
                    val = False
                else:
                    raise Exception("Invalid boolean value " + input)
            elif assignee_type == 'int':
                val = int(input)
            elif assignee_type == 'float':
                val = float(input)
            elif assignee_type == 'string':
                val = str(input)
            else:
                raise Exception("Invalid input type at assignment " + input)

            address = last_symbol_table().add_sym(str(val), assignee_type, is_constant=True)
            quadruples.append(['=', address, '', assignee_address])
            print()
        elif isinstance(self.value, NewObject):
            assignee_address, assignee_type = last_symbol_table().get_sym_address_and_type(self.id)

            if assignee_type != self.value.type:
                raise Exception("Invalid assignment of object of type {0} to variable of type {1}"
                                .format(self.value.type, assignee_type))

            # Flag that indicates if this symbol is of global scope or local (function) scope,
            is_global = last_symbol_table().is_global(self.id)

            quadruples.append(['NEW_OBJ', self.value.type, assignee_address, is_global])

            # Get the class model for this object type.
            class_model = None
            for table in final_sym_tables:
                if table.cid == assignee_type:
                    class_model: Class = table.class_model

            if class_model is None:
                raise Exception("Illegal state: class_model should not be None")

            if len(class_model.members) != len(self.value.members):
                raise Exception("Constructor of class {0} expected {1} arguments but found {2}"
                                .format(assignee_type, len(class_model.members), len(self.value.members)))

            for param_index in range(0, len(self.value.members)):
                param = self.value.members[param_index]
                address, type = param.eval()

                if class_model.members[param_index].type != type:
                    if type != "NULL":
                        raise Exception("{0} class constructor expected argument of type {1} at pos({2}) but found {3}"
                                    .format(assignee_type, class_model.members[param_index].type, param_index, type))

                quadruples.append(['OBJ_MEMBER', address, '', 'objMember' + str(param_index)])
                param_index += 1

            for i in range(0, len(quadruples)):
                quad = quadruples[i]
                if quad[0] == 'START_CLASS' and quad[1] == self.value.type:
                    class_start_quad_index = i
                    break
            quadruples.append(['OBJ_CONST', self.value.type, assignee_address, class_start_quad_index])
        else:
            address, type = self.value.eval()  # address and type of the result.

            # Verify that the variable to assign to exists and is of correct type. Throws if invalid.
            is_global = last_symbol_table().verify_sym_declared_with_correct_type(self.id,
                                                                                  utils.parser_type_to_cube_type(type))

            assignee_address, assignee_type = last_symbol_table().get_sym_address_and_type(self.id)

            quadruples.append(['=', address, is_global, assignee_address])


class ConstantVar(BaseExpression):
    def __init__(self, varcte, type):
        self.varcte = varcte
        self.type = type

    def __repr__(self):
        return '<ConstantVar varcte={0} type={1}>'.format(self.varcte, self.type)

    def eval(self):
        if self.type == "ID":
            return last_symbol_table().get_sym_address_and_type(self.varcte)

        if self.type == "NULL":
            return None, "NULL"

        # Varcte if a primitive
        cube_type = utils.parser_type_to_cube_type(self.type)

        # Add constant primititive to symbol table with its a value as its name.
        # e.g. for varcte = 5 of type INTNUM, call add_sym('5', 'int').
        # This creates a record(memory address) in the symbol table for the constant 5 indexed as '5'.
        address = last_symbol_table().add_sym(str(self.varcte), cube_type, is_constant=True)
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
        return '<TerminoR optype={0} factor={1} termino_r={2}>' \
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
            address = last_symbol_table().add_temp(res_type)
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
            address = last_symbol_table().add_temp(res_type)
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
            address = last_symbol_table().add_temp(res_type)
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
            address = last_symbol_table().add_temp(res_type)
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

            # If both operands are not primitives (meaning they're objects or null) and the operators are of equality,
            # then the resulting type is a boolean.
            if left_type not in cube.keys() and right_type not in cube.keys() and (op_type == "==" or op_type == "!="):
                res_type = "bool"
            else:
                res_type = cube[left_type][right_type][op_type]
            if res_type is "Error":
                raise Exception("Invalid operation {0} for {1} and {2}".format(op_type, left_type, right_type))

            # Add a temp var to the symbol table for the result of the operation e.g. t1 in (+ a b t1)
            address = last_symbol_table().add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class LogicalOperand(BaseExpression):
    def __init__(self, type, super_exp: RelationalOperation, logical_operand: BaseExpression):
        self.type = type
        self.super_exp = super_exp
        self.logical_operand = logical_operand

    def __repr__(self):
        return '<LogicalOperand type={0} super_exp={1} logical_operand={2}>' \
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
            address = last_symbol_table().add_temp(res_type)
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
            address = last_symbol_table().add_temp(res_type)
            quadruples.append([op_type, left_address, right_address, address])
            return address, res_type


class If(BaseExpression):
    def __init__(self, base_exp: BaseExpression, true_stmts: List[BaseExpression], false_stmts: List[BaseExpression]):
        self.base_exp = base_exp
        self.true_stmts = true_stmts
        self.false_stmts = false_stmts

    def __repr__(self):
        return '<If base_exp={0} true_stms={1}>' \
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
        one_const_address, one_const_type = last_symbol_table().get_sym_address_and_type('1')

        start_address, start_type, end_address, end_type = self.range.eval()
        id_address, id_type = last_symbol_table().get_sym_address_and_type(self.id)

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
        address = last_symbol_table().add_temp(res_type)
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
        address = last_symbol_table().add_temp(res_type_2)
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


class WhenBranch(BaseExpression):
    def __init__(self, base_exp: BaseExpression, stmts: List[BaseExpression], next_branch: BaseExpression):
        self.base_exp = base_exp
        self.stmts = stmts
        self.next_branch = next_branch

    def __repr__(self):
        return '<WhenBranch base_exp={0} stmts={1} next_branch={2}>' \
            .format(self.base_exp, self.stmts, self.next_branch)

    def eval(self):
        if self.base_exp is not None:
            exp_address, exp_type = self.base_exp.eval()
            if exp_type != 'bool':
                raise Exception("When branch must evaluate to bool")

            gotof = ["GOTOF", exp_address, '', '']
            quadruples.append(gotof)

            for stmt in self.stmts:
                stmt.eval()

            goto = ["GOTO", '', '', '']
            quadruples.append(goto)

            gotof[3] = len(quadruples)

            if self.next_branch is not None:
                self.next_branch.eval()

            goto[3] = len(quadruples)
        else:
            for stmt in self.stmts:
                stmt.eval()

            goto = ["GOTO", '', '', '']
            quadruples.append(goto)
            goto[3] = len(quadruples)


class Write(BaseExpression):
    def __init__(self, args: List[BaseExpression]):
        self.args = args

    def __repr__(self):
        return '<Write args={0}>'.format(self.args)

    def eval(self):
        for arg in self.args:
            address, _ = arg.eval()
            quadruples.append(['WRITE', address, '', ''])
        quadruples.append(['WRITE', '', '', ''])


class Read(BaseExpression):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '<Read message={0}>'.format(self.message)

    def eval(self):
        if self.message is None:
            return input()
        return input(self.message)


class ObjectMember(BaseExpression):
    def __init__(self, object, member):
        self.object = object
        self.member = member

    def __repr__(self):
        return '<ObjectMember object={0} member={1}>'.format(self.object, self.member)

    def eval(self):
        # Find the type and address of the object.
        obj_address, obj_type = last_symbol_table().get_sym_address_and_type(self.object)

        # Find the type and address of the member of the object.
        member_type = None
        member_address = None
        for symbol_table in final_sym_tables:
            if symbol_table.cid == obj_type:
                for type in symbol_table.get_global_table().keys():
                    if self.member in symbol_table.get_global_table()[type]:
                        member_type = type
                        member_address = symbol_table.get_global_table()[type][self.member]
                        break

        if obj_address is None or member_address is None:
            raise Exception("Illegal State: Object and member address should not be None.")

        # The temp address where the value of object.member will be stored.
        temp_res_address = last_symbol_table().add_temp(member_type)

        quadruples.append(['GET_OBJ_MEM', obj_address, member_address, temp_res_address])
        return temp_res_address, member_type


class NewObject(BaseExpression):
    def __init__(self, type, members: List[BaseExpression]):
        self.type = type
        self.members = members

    def __repr__(self):
        return '<NewObject type={0} members={1}>'.format(self.type, self.members)

    def eval(self):
        for member in self.members:
            member.eval()
