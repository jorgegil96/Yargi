from argparse import ArgumentParser

from src.parser import parser
from src.semantics import model
from src.semantics.model import *
from src.virtualmachine.VirtualMachine import VirtualMachine

arg_parser = ArgumentParser()
arg_parser.add_argument("-f", "--file", help='Source file', type=str)
arg_parser.add_argument("-q", "--quad", help='Print quadruples?', type=bool, default=False)

args = arg_parser.parse_args()

with open(args.file) as f:
    input = f.read()

    interfaces, classes = parser.parse(input)

    model.quadruples.append(['GOTO', '', '', ''])

    for interface in interfaces:
        interface.eval()
    for cls in classes:
        cls.eval()

    if args.quad:
        for i in range(0, len(quadruples)):
            print(str(i) + ": " + str(quadruples[i]))

    print("Compilation finished with no errors")
    print()

    print("Executing...\n")
    vm = VirtualMachine(model.quadruples, model.final_sym_tables)
    vm.execute()
    print("\nExecution finished")
