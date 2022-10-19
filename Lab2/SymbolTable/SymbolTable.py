import sys

class SymbolTable:
    def __init__(self):
        self.arr = [-sys.maxsize] * 10000


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
                return index
        for index in range(0, elementHash-1):
            if self.arr[index] == -sys.maxsize:
                self.arr[index] = element
                return index
        return -69
            

    def store(self, element):
        elementHash = self.__hashFunction(element)
        if self.arr[elementHash] == -sys.maxsize:
            self.arr[elementHash] = element
            return elementHash
        elif self.arr[elementHash] == element:
            return elementHash
        return self.__solveStoreConflict(element, elementHash)