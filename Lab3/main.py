import sys
from typing import Tuple
from DataStructures.ProgramInternalForm import ProgramInternalForm
from DataStructures.SymbolTable import SymbolTable
from Exceptions.Exception import LexicalError
from utils.colors import ConsoleColors
from utils.read_tokens import read_tokens
from nltk.tokenize import word_tokenize
import nltk
import re
# REQ 1-B

TOKEN_LIST = read_tokens()
STC = SymbolTable()
STI = SymbolTable()
PIF = ProgramInternalForm()


def isIdentifier(word: str):
    return re.match("^[a-zA-Z][a-zA-Z0-9]*$", word)


def isNumberConstant(word: str):
    return re.match("^[\d]*$", word)


def correctlyFormedString(word: str):
    return re.match("^\"([a-zA-z0-9_ ]*)\"$", word)


def tokenizeLine(text: str, lineIndex: int):
    text = text.strip()
    if text.startswith("##") and text in TOKEN_LIST:
        PIF.store((text, -1))
    else:
        if not "\"" in text:
            text = word_tokenize(text)
        else:
            text = text.split()
        i = 0
        while i < len(text):
            token = text[i]
            if token in "><=!" and text[i+1] in "><=!":
                token = token + text[i+1]
                i = i + 2
            if token in TOKEN_LIST:
                PIF.store((token, -1))
            else:
                if correctlyFormedString(token):
                    index = STC.store(token)
                    PIF.store(("const", index))
                elif isNumberConstant(token):
                    index = STC.store(token)
                    PIF.store(("const", index))
                elif isIdentifier(token):
                    index = STI.store(token)
                    PIF.store(("id", index))
                else: raise LexicalError("Lexical error at line "+str(lineIndex)+". Unrecognized token `"+token+"`")
            i += 1


def main():
    programFileName = input("Enter program file name:")

    lineIndex = 0
    with open(programFileName) as programFile:
        for line in programFile:
            lineIndex += 1
            if line == "\n" or line == " " or line == "\t" or line.strip().startswith("//"):
                pass
            else:
                try: tokenizeLine(line, lineIndex)
                except LexicalError as le: 
                    print(ConsoleColors.FAIL+"\t>>>"+str(le)+ConsoleColors.ENDC)
                    exit()

    PIF.outputToFile("PIF.out")
    STC.outputToFile("STC.out")
    STI.outputToFile("STI.out")
    return 0


if (main() == 0):
    print(ConsoleColors.OKGREEN+"\t>>>Successful run"+ConsoleColors.ENDC)
