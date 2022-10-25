import sys
from SymbolTable.SymbolTable import SymbolTable

# REQ 1-B

sti = SymbolTable()
stc = SymbolTable()

try:
    stc.store("da")
    stc.store("ad")
    stc.store("bc")
    stc.store("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
except IndexError:
    print("Index out of bounds")


for el in stc.arr:
    if el != -sys.maxsize:
        print(el)