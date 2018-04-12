from semantics.SymbolTable import *


class SemanticAnalyser:
    def __init__(self):
        self.quadruples = []
        self.symbol_table = SymbolTable()
