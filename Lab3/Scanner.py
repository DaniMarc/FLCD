from Exceptions.Exception import LexicalError
from nltk.tokenize import word_tokenize
import re

class Scanner:
    def __init__(self) -> None:
        pass
    
    
    def __isIdentifier(self, word: str):
        return re.match("^[a-zA-Z][a-zA-Z0-9]*$", word)


    def __isNumberConstant(self, word: str):
        return re.match("^[\d]*$", word)


    def __correctlyFormedString(self, word: str):
        return re.match("^\"([a-zA-z0-9_ ]*)\"$", word)


    def scan(self, text: str, lineIndex: int, TOKEN_LIST, STC, STI, PIF):
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
                    if self.__correctlyFormedString(token):
                        index = STC.store(token)
                        PIF.store(("const", index))
                    elif self.__isNumberConstant(token):
                        index = STC.store(token)
                        PIF.store(("const", index))
                    elif self.__isIdentifier(token):
                        index = STI.store(token)
                        PIF.store(("id", index))
                    else: raise LexicalError("Lexical error at line "+str(lineIndex)+". Unrecognized token `"+token+"`")
                i += 1