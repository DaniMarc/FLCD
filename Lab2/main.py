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
except IndexError or ValueError as e:
    print(e)


for el in stc.arr:
    if el != -sys.maxsize:
        print(el)