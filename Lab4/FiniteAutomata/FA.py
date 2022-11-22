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
                        self.__transitions.append(
                            (transition[0], transition[1], transition[2]))
                    lineIndex += 1

    def __getNextState(self, currentState, character):
        for transition in self.__transitions:
            if transition[0] == currentState and transition[2] == character:
                if len(transition[1]) == 1:
                    return transition[1]
        return "noState"

    def __isDFA(self, sequence):
        # TODO
        pass

    def __isAccepted(self, sequence):
        if self.__isDFA(sequence):
            currentState = self.__initialState
            for character in sequence:
                nextState = self.__getNextState(currentState, character)
                if nextState == "noState":
                    return False
                currentState = nextState
            return currentState in self.__finalStates
        return False

    def __printMenu(self):
        print("\n1. Set of states")
        print("2. The alphabet")
        print("3. All of the transitions")
        print("4. Initial state and final states")
        print("5. Test if sequence is accepted by the FA")
        print("0. Exit\n")
        return

    def __printStates(self):
        print("\t>>>The set of states is: "+str(self.__states))

    def __printAlphabet(self):
        print("\t>>>The alphabet is:"+str(self.__alphabet))

    def __printTransitions(self):
        for trans in self.__transitions:
            print("\t δ("+str(trans[0])+", " +
                  str(trans[2])+") -> "+str(trans[1]))

    def __printInitialFinal(self):
        print("\t Initial state is: "+str(self.__initialState))
        print("\t Final states are: "+str(self.__finalStates))

    def __testFA(self):
        seq = input("Enter sequence: ")
        print("\t The automaton accepts your sequence: " +
              str(self.__isAccepted(seq)))

    def FAMenu(self):
        command = None
        while True:
            try:
                self.__printMenu()
                command = int(input("Waiting for command: "))
                if command == 1:
                    self.__printStates()
                elif command == 2:
                    self.__printAlphabet()
                elif command == 3:
                    self.__printTransitions()
                elif command == 4:
                    self.__printInitialFinal()
                elif command == 5:
                    self.__testFA()
                elif command == 0:
                    break
            except ValueError as ve:
                print("Invalid input")

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
FA.FAMenu()
