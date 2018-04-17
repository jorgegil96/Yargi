import operator


def parser_type_to_cube_type(type):
    if type in ['int', 'float', 'bool', 'string']:
        return type
    if type == "TRUE" or type == "FALSE":
        return "bool"
    elif type == "INTNUM":
        return "int"
    elif type == "FLOATNUM":
        return "float"
    elif type == "STRINGVAL":
        return "string"
    else:
        raise Exception("Invalid type %s" % type)


def operator_from_symbol(symbol):
    if symbol == '+':
        return operator.add
    elif symbol == '-':
        return operator.sub
    elif symbol == '*':
        return operator.mul
    elif symbol == '/':
        return operator.floordiv
    elif symbol == '>':
        return operator.gt
    elif symbol == '<':
        return operator.lt
    elif symbol == '>=':
        return operator.ge
    elif symbol == '<=':
        return operator.le
    elif symbol == '==':
        return operator.eq
    elif symbol == '!=':
        return operator.ne
