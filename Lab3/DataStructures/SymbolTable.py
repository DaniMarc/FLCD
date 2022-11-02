import sys

class SymbolTable:
    def __init__(self):
        self.__arr = [-sys.maxsize] * 10000
        self.elementsCount = 0


    def getArray(self):
        return self.__arr


    def __hashFunction(self, element):
        strElement = str(element)
        asciiSum = 0
        for e in strElement:
            asciiSum += ord(e)
        return asciiSum


    def __solveStoreConflict(self, element, elementHash):
        for index in range(elementHash, len(self.__arr)-1):
            if self.__arr[index] == -sys.maxsize:
                self.__arr[index] = element
                self.elementsCount += 1
                return index
        for index in range(0, elementHash):
            if self.__arr[index] == -sys.maxsize:
                self.__arr[index] = element
                self.elementsCount += 1
                return index
        return -69
            

    def store(self, element):
        if self.elementsCount != len(self.__arr):
            elementHash = self.__hashFunction(element)
            if elementHash > len(self.__arr): elementHash = 0
            if self.__arr[elementHash] == -sys.maxsize:
                self.__arr[elementHash] = element
                self.elementsCount += 1
                return elementHash
            elif self.__arr[elementHash] == element:
                return elementHash
            return self.__solveStoreConflict(element, elementHash)
        else: raise ValueError("Symbol table is full")

    
    def outputToFile(self, filename):
        with open(filename, "w") as out:
            for item in self.__arr:
                if item != -sys.maxsize:
                    out.write(item+" "+str(self.__arr.index(item))+"\n")
