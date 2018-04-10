from model import *
from typing import List

VAR_SCOPE_GLOBAL = 1
VAR_SCOPE_LOCAL = 2


class SemanticAnalyser:
    def __init__(self, class_body: ClassBody):
        self.class_body = class_body
        self.global_vars = {}
        self.local_vars = {}
        self.funs_dir = {}

    def verify(self):
        # Verify global variables
        self.verify_vars(self.class_body.vars, VAR_SCOPE_GLOBAL)

        # Verify every function
        for fun in self.class_body.funs:
            self.verify_fun(fun)
            self.local_vars.clear()

    def verify_vars(self, vars: List[VarDeclaration], scope: int):
        if scope == VAR_SCOPE_GLOBAL:
            for var in vars:
                if var.name in self.global_vars:
                    raise Exception("Variable %s is already declared" % var.name)
                else:
                    self.global_vars[var.name] = var
        elif scope == VAR_SCOPE_LOCAL:
            for var in vars:
                if var.name in self.local_vars:
                    raise Exception("Variable %s is already declared" % var.name)
                else:
                    self.local_vars[var.name] = var
        else:
            raise Exception("Invalid scope %s" % scope)

    @staticmethod
    def is_var_declared(id, var_table: dict):
        return id in var_table

    def get_ids_in_expr(self, exp_r: ExpR):
        if exp_r is None:
            return []
        return self.get_ids_in_termino(exp_r.termino) + self.get_ids_in_expr(exp_r.exp_r)

    def get_ids_in_termino(self, termino: Termino):
        ids = []
        factor = termino.factor
        if isinstance(factor, ConstantVar):
            id = factor.varcte
            if factor.type == "ID":
                ids.append(id)
        elif isinstance(factor, ArithmeticOperand):
            id = factor.varcte
            if factor.type == "ID":
                ids.append(id)
        return ids

    def get_ids_in_exp(self, exp: Exp):
        return self.get_ids_in_termino(exp.termino) + self.get_ids_in_expr(exp.exp_r)

    def verify_fun(self, fun: Fun):
        if fun.name in self.funs_dir:
            raise Exception("Function %s is already defined" % fun.name)
        else:
            self.funs_dir[fun.name] = fun
        self.verify_vars(fun.body.vars, VAR_SCOPE_LOCAL)

        for stmt in fun.body.statements:
            if isinstance(stmt, Assignment):
                # Verify that the variable to assign to exists.
                if not self.is_var_declared(stmt.id, self.local_vars):
                    raise Exception("Use of undeclared variable %s" % stmt.id)

                log_op: LogicalOperation = stmt.value
                log_operand: LogicalOperand = log_op.logical_operand
                if log_operand is not None:
                    log_op_type = log_operand.type  # and, or

                rel_op: RelationalOperation = log_op.super_exp
                rel_operand: RelationalOperand = rel_op.relational_operand
                if rel_operand is not None:
                    rel_op_type = rel_operand.type  # >, < etc..

                exp: Exp = rel_op.exp
                for id in self.get_ids_in_exp(exp):
                    if not self.is_var_declared(id, self.local_vars) \
                            and not self.is_var_declared(id, self.global_vars):
                        raise Exception("Use of undeclared variable %s" % id)
