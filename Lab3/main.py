import sys
from typing import Tuple
from DataStructures.ProgramInternalForm import ProgramInternalForm
from DataStructures.SymbolTable import SymbolTable
from Exceptions.Exception import LexicalError
from Scanner import Scanner
from utils.colors import ConsoleColors
from utils.read_tokens import read_tokens

# REQ 1-B

TOKEN_LIST = read_tokens()
STC = SymbolTable()
STI = SymbolTable()
PIF = ProgramInternalForm()


def main():
    programFileName = input("Enter program file name: ")

    scanner = Scanner()

    lineIndex = 0
    with open(programFileName) as programFile:
        for line in programFile:
            lineIndex += 1
            if line == "\n" or line == " " or line == "\t" or line.strip().startswith("//"):
                pass
            else:
                try: scanner.scan(line, lineIndex, TOKEN_LIST, STC, STI, PIF)
                except LexicalError as le: 
                    print(ConsoleColors.FAIL+"\t>>>"+str(le)+ConsoleColors.ENDC)
                    exit()

    PIF.outputToFile("PIF.out")
    STC.outputToFile("STC.out")
    STI.outputToFile("STI.out")
    return 0


if (main() == 0):
    print(ConsoleColors.OKGREEN+"\t>>>Successful run"+ConsoleColors.ENDC)
