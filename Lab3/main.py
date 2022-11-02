import sys
from typing import Tuple
from DataStructures.ProgramInternalForm import ProgramInternalForm
from DataStructures.SymbolTable import SymbolTable
from utils.read_tokens import read_tokens
from nltk.tokenize import word_tokenize
import nltk
import re

# REQ 1-B

TOKEN_LIST = read_tokens()
STC = SymbolTable()
STI = SymbolTable()
PIF = ProgramInternalForm()

print(word_tokenize("\"hello my darling! >= \n asd", preserve_line=True))


def isIdentifier(word:str):
    return re.match("^[a-zA-Z][a-zA-Z0-9]*$", word)


def isNumberConstant(word:str):
    return re.match("^[\d]*$", word)


def correctlyFormedString(word:str):
    return re.match("^\"([a-zA-z0-9_ ]*)\"$", word)


def tokenizeLine(text:str):
    text = text.strip()
    if text.startswith("##") and text in TOKEN_LIST:
        PIF.store((text, -1))
    else:
        if not "\"" in text:
            text = word_tokenize(text)
        else: 
            text = text.split()
        for token in text:
            if token in TOKEN_LIST:
                PIF.store((token, -1))
            else:
                if correctlyFormedString(token):
                    index = STC.store(token)
                    PIF.store(("const"+str(token), index))
                elif isNumberConstant(token):
                    index = STC.store(token)
                    PIF.store(("const"+str(token), index))
                elif isIdentifier(token):
                    index = STI.store(token)
                    PIF.store(("id--"+str(token), index))

    
def main():
    programFileName = input("Enter program file name:")

    index = 0;
    with open(programFileName) as programFile:
        for line in programFile:
            index += 1
            if line == "\n" or line == " " or line == "\t":
                pass
            else: tokenizeLine(line)

    # try:
    #     stc.store("da")
    #     stc.store("ad")
    #     stc.store("bc")
    #     sti.store("ay")
    # except IndexError or ValueError as e:
    #     print(e)
    # stc.outputToFile("STC.out")
    # sti.outputToFile("STI.out")

    # PIF.store(("id", 0))
    # PIF.store(("#", -1))
    # PIF.store(("#", -1))
    PIF.outputToFile("PIF.out")
    STC.outputToFile("STC.out")
    STI.outputToFile("STI.out")
    return 0



if(main() == 0):
    print("\t>>>Successful run")
