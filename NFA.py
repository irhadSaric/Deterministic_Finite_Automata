from DFA import *

class NFA(DFA):
    def __init__(self):
        DFA.__init__()

    def __init__(self, listOfStates : list, startingState : State):
        DFA.__init__(listOfStates, startingState)

    def convertToDFA(self):
        pass
