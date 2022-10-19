import sys
from SymbolTable.SymbolTable import SymbolTable

# REQ 1B

sti = SymbolTable()
stc = SymbolTable()

stc.store("da")
stc.store("ad")
stc.store("bc")
stc.store("ni")

for el in stc.arr:
    if el != -sys.maxsize:
        print(el)