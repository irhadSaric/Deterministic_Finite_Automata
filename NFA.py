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

        """for i in result:
            print(i)
        """

    def __partitions(self) -> list:
        from itertools import combinations
        result = []

        for j in range(1, self.dictOfStates.__len__()):
            for i in combinations(self.dictOfStates.keys(), j):
                temp = []
                for k in range(0, len(i)):
                    temp.append(i[k])
                result.append(temp)

        return result

    def convertToDFA(self):
        allStates = self.__partitions()
        dictOfPartitions = {}
        counter = 0
        for i in allStates:
            tuple = (*i, -2)
            dictOfPartitions[tuple] = counter
            counter += 1
        dictOfPartitions[(-1, -2)] = counter
        #print(dict)

        dfaDict = {}
        for i in dictOfPartitions:
            #print(self.dictOfStates)
            counter = 0
            startingCoordinateInTuple = i[counter]
            tempDict = {}
            tempDict[i] = []
            while startingCoordinateInTuple != -2:
                for j in self.alphabet:
                    if(startingCoordinateInTuple == -1):
                        break
                    if(j not in self.dictOfStates[startingCoordinateInTuple].transitions):
                        tempDict[i].append("Mrs")
                    else:
                        tempDict[i].append(self.dictOfStates[startingCoordinateInTuple].transitions[j])
                counter += 1
                startingCoordinateInTuple = i[counter]
            #print(tempDict)
            dfaDict[dictOfPartitions[i]] = tempDict
        print(dfaDict)