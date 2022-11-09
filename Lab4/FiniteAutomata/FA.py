class FiniteAutomata:
    def __init__(self) -> None:
        self.__states = []
        self.__alphabet = []
        self.__initialState = None
        self.__finalStates = []
        self.__transitions = []
        self.__initAutomata()

    def __initAutomata(self):
        with open("FA.in") as lines:
            lineIndex = 1
            for line in lines:
                if not (line == "\n" or line == " " or line == ""):
                    if lineIndex == 1:
                        self.__states = line.split()
                    elif lineIndex == 2:
                        self.__alphabet = line.split()
                    elif lineIndex == 3:
                        self.__initialState = line.split()[0]
                    elif lineIndex == 4:
                        self.__finalStates = line.split()
                    else:
                        transition = line.split()
                        self.__transitions.append((transition[0], transition[1], transition[2]))
                    lineIndex += 1


    def getStates(self):
        return self.__states

    
    def getAlphabet(self):
        return self.__alphabet


    def getInitialState(self):
        return self.__initialState


    def getFinalStates(self):
        return self.__finalStates

    
    def getTransitions(self):
        return self.__transitions




FA = FiniteAutomata()
print("read")
    