import sys

class SymbolTable:
    def __init__(self):
        self.arr = [-sys.maxsize] * 100000
        self.elementsCount = 0


    def getArray(self):
        return self.arr


    def __hashFunction(self, element):
        strElement = str(element)
        asciiSum = 0
        for e in strElement:
            asciiSum += ord(e)
        return asciiSum


    def __solveStoreConflict(self, element, elementHash):
        for index in range(elementHash, len(self.arr)-1):
            if self.arr[index] == -sys.maxsize:
                self.arr[index] = element
                self.elementsCount += 1
                return index
        for index in range(0, elementHash):
            if self.arr[index] == -sys.maxsize:
                self.arr[index] = element
                self.elementsCount += 1
                return index
        return -69
            

    def store(self, element):
        if self.elementsCount != len(self.arr):
            elementHash = self.__hashFunction(element)
            if elementHash > len(self.arr): elementHash = 0
            if self.arr[elementHash] == -sys.maxsize:
                self.arr[elementHash] = element
                self.elementsCount += 1
                return elementHash
            elif self.arr[elementHash] == element:
                return elementHash
            return self.__solveStoreConflict(element, elementHash)
        else: raise ValueError("Symbol table is full")
