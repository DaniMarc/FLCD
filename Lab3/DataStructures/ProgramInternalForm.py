from typing import Tuple


class ProgramInternalForm:
    def __init__(self):
        self.__arr = []

    def getPIF(self):
        return self.__arr

    def store(self, newPair):
        if type(newPair) != tuple:
            raise TypeError("The item that is added in the PIF must be a tuple")
        self.__arr.append(newPair)

    def outputToFile(self, filename):
        with open(filename, "w") as out:
            for item in self.__arr:
                # print(str(type(item[0])) + item[0])
                out.write(item[0]+" "+str(item[1])+"\n")