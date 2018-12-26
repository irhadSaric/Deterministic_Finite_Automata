from DFA import *

class NFA(DFA):
    def __init__(self):
        super(NFA, self).__init__()

    def __init__(self, dictOfStates : dict, startingState : State, alphabet: list):
        super(NFA, self).__init__(dictOfStates, startingState, alphabet)

    def __stateNumber(self, number: int) -> State:
        return self.dictOfStates[number]

    def __accepts_rek(self, startingState: State, string: str, indexOfCurrentSymbol: int):
        #print(startingState.stateNumber, indexOfCurrentSymbol)
        if indexOfCurrentSymbol == len(string):
            if startingState.isFinalState:
                return True
            if indexOfCurrentSymbol >= len(string):
                return

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

        return result

        """for i in result:
            print(i)
        """

    def __partitions(self) -> list:
        from itertools import combinations
        result = []

        for j in range(1, self.dictOfStates.__len__()+1):
            for i in combinations(self.dictOfStates.keys(), j):
                temp = []
                for k in range(0, len(i)):
                    temp.append(i[k])
                result.append(temp)

        return result

    def convertToDFA(self) -> DFA:
        allStates = self.__partitions()
        dictOfPartitions = {}
        counter = 0
        for i in allStates:
            Tuple = (*i, -2)
            dictOfPartitions[Tuple] = counter
            counter += 1
        dictOfPartitions[(-1, -2)] = counter

        dfaDict = {}
        for i in dictOfPartitions:
            counter = 0
            startingCoordinateInTuple = i[counter]
            tempDict = {}
            tempDict[i] = []
            while startingCoordinateInTuple != -2:
                for j in self.alphabet:
                    if(startingCoordinateInTuple == -1):
                        break
                    else:
                        if(j not in self.dictOfStates[startingCoordinateInTuple].transitions):
                            tempDict[i].append([-1337])#Ako nema grana iz stanja za znak iz alfabeta
                        else:
                            tempDict[i].append(self.dictOfStates[startingCoordinateInTuple].transitions[j])
                    for element in self.allStatesUsingOnlyEpsilonEdges(self.dictOfStates[startingCoordinateInTuple]):
                        tempDict[i][0].append(element)
                        #print(tempDict)
                counter += 1
                startingCoordinateInTuple = i[counter]
            dfaDict[dictOfPartitions[i]] = tempDict
        #print(dfaDict)

        #print(dfaDict)
        resultDict = {}
        for i in dfaDict:
            for k in dfaDict[i]:
                resultDict[k] = []
                for f in range(0, len(self.alphabet)):
                    lista = []
                    for element in range(0+f, len(dfaDict[i][k]), len(self.alphabet)):
                        #if(dfaDict[i][k][element] == -1337):
                        #    dfaDict[i][k][element] = [dfaDict[i][k][element]]
                        #print(lista)
                        lista = lista + dfaDict[i][k][element]
                    resultDict[k].append(list(set(lista)))
                #print(resultDict[k])

       # print("----")
        #print(resultDict)
        for i in resultDict:
            for j in resultDict[i]:
                if j == [-1337]:
                    j[0] = -1
                if i != (-1, -2) and j[-1] == -1337:
                    del j[-1]
                j.append(-2)
        #print(resultDict)
        tempResult = {}
        for i in resultDict:
            if i == (-1, -2):
                tempResult[i] = [(-1, -2), (-1, -2)]
            else:
                tempList = []
                for j in resultDict[i]:
                    tempList2 = sorted(j[0:len(j)-1])
                    tempList2 += [j[len(j)-1]]
                    if tempList2[0] == -1337:
                        del tempList2[0]
                    tempTuple = tuple(tempList2)
                    tempList.append(tempTuple)
                tempResult[i] = tempList
        converted = {}
        #print(dictOfPartitions)
        for i in tempResult.keys():
            tempDictOfTransitions = {}
            tempBool = False
            for index, symbol in enumerate(self.alphabet):
                tempDictOfTransitions[symbol] = dictOfPartitions[tempResult[i][index]]
            for j in i:
                if j != -1 and j != -2:
                    if self.dictOfStates[j].isFinalState:
                        tempBool = True
            converted[dictOfPartitions[i]] = State(dictOfPartitions[i], tempBool, tempDictOfTransitions)

        help = sorted(self.allStatesUsingOnlyEpsilonEdges(self.__stateNumber(list(self.dictOfStates.keys())[0])))
        help.append(-2)
        startingNFAState = tuple(help)
        startingNFAState = dictOfPartitions[startingNFAState]
        startingNFAState = converted[startingNFAState]
        finalDFA = DFA(converted, startingNFAState, self.alphabet)
        return finalDFA