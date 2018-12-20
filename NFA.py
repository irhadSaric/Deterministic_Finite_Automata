from DFA import *

class NFA(DFA):
    def __init__(self):
        DFA.__init__()

    def __init__(self, dictOfStates : dict, startingState : State, alphabet: list):
        DFA.__init__(self, dictOfStates, startingState, alphabet)

    def __stateNumber(self, number: int) -> State:
        return self.dictOfStates[number]

    def __accepts_rek(self, startingState: State, string: str, indexOfCurrentSymbol: int):
        print(startingState.stateNumber, string, indexOfCurrentSymbol)
        if indexOfCurrentSymbol == len(string):
            if startingState.isFinalState:
                return True

        symbol = string[indexOfCurrentSymbol]
        if not symbol.isalpha():
            symbol = int(symbol)

        if startingState.transitions:
            if symbol in startingState.transitions:
            #print(symbol, startingState.stateNumber, indexOfCurrentSymbol)
                for i in startingState.transitions[symbol]:
                    if(self.__accepts_rek(self.__stateNumber(i), string, indexOfCurrentSymbol + 1)):
                        return True

    def accepts(self, string: str):
        return self.__accepts_rek(self.startingState, string, 0)

