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
            if "epsilon" in startingState.transitions:
              for i in startingState.transitions["epsilon"]:
                    if(self.__accepts_rek(self.__stateNumber(i), string, indexOfCurrentSymbol)):
                        return True
            if symbol in startingState.transitions:
            #print(symbol, startingState.stateNumber, indexOfCurrentSymbol)
                for i in startingState.transitions[symbol]:
                    if(self.__accepts_rek(self.__stateNumber(i), string, indexOfCurrentSymbol + 1)):
                        return True

    def accepts(self, string: str) -> bool:
        return self.__accepts_rek(self.startingState, string, 0)

    def allStatesUsingOnlyEpsilonEdges(self, state: State) -> list:
        queue = []
        result = []
        queue.append(state)
        result.append(state.stateNumber)
        while len(queue) != 0:
            if "epsilon" in queue[0].transitions:
                for i in queue[0].transitions["epsilon"]:
                    queue.append(self.__stateNumber(i))
                    result.append(i)
            queue.pop(0)

        for i in result:
            print(i)