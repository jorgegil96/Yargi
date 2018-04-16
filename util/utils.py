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
