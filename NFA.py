from DFA import *

class NFA(DFA):
    def __init__(self):
        super(NFA, self).__init__()

    def __init__(self, dictOfStates : dict, startingState : State, alphabet: list):
        super(NFA, self).__init__(dictOfStates, startingState, alphabet)

    def __stateNumber(self, number: int) -> State:
        return self.dictOfStates[number]

    def __accepts_rek(self, startingState: State, string: str, indexOfCurrentSymbol: int) -> bool:
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

    def __makeDictOfPartitions(self, partitions: list) -> dict:
        dictOfPartitions = {}
        counter = 0
        for i in partitions:
            Tuple = (*i, -2)
            dictOfPartitions[Tuple] = counter
            counter += 1
        dictOfPartitions[(-1, -2)] = counter
        return dictOfPartitions

    def __makeDFAdict(self, dictOfPartitions: dict) -> dict:
        dfaDict = {}
        for i in dictOfPartitions:
            counter = 0
            startingCoordinateInTuple = i[counter]
            tempDict = {}
            tempDict[i] = []
            while startingCoordinateInTuple != -2 and startingCoordinateInTuple != -1:
                for c2, j in enumerate(self.alphabet):
                    if startingCoordinateInTuple == -1 or startingCoordinateInTuple == -2:
                        break
                    else:
                        if j not in self.dictOfStates[startingCoordinateInTuple].transitions:
                            tempDict[i].append([-1337])#Ako nema grana iz stanja za znak iz alfabeta
                        else:
                            tempDict[i].append(self.dictOfStates[startingCoordinateInTuple].transitions[j])
                for c2, j in enumerate(tempDict[i]):
                    tempListEpsilonStates = []
                    for state in j:
                        if state != -1337 and state != -1 and state != -2:
                            tempListEpsilonStates += self.allStatesUsingOnlyEpsilonEdges(self.dictOfStates[state])
                            tempDict[i][c2] = tempListEpsilonStates
                counter += 1
                startingCoordinateInTuple = i[counter]
            dfaDict[dictOfPartitions[i]] = tempDict
        return dfaDict

    def __mergeTransitions(self, dfaDict: dict) -> dict:
        resultDict = {}
        for i in dfaDict:
            for k in dfaDict[i]:
                resultDict[k] = []
                for f in range(0, len(self.alphabet)):
                    lista = []
                    for element in range(0 + f, len(dfaDict[i][k]), len(self.alphabet)):
                        lista = lista + dfaDict[i][k][element]
                    resultDict[k].append(list(set(lista)))
                # print(resultDict[k])
        return resultDict

    def __simplify(self, mergedTransitionsInDfaDict: dict) -> dict:
        for i in mergedTransitionsInDfaDict:
            for j in mergedTransitionsInDfaDict[i]:
                if j == [-1337]:
                    j[0] = -1
                if i != (-1, -2) and j[-1] == -1337:
                    del j[-1]
                j.append(-2)
        return mergedTransitionsInDfaDict

    def __transitionsToTuples(self, mergedTransitionsInDfaDict: dict) -> dict:
        tempResult = {}
        for i in mergedTransitionsInDfaDict:
            if i == (-1, -2):
                tempResult[i] = [(-1, -2), (-1, -2)]
            else:
                tempList = []
                for j in mergedTransitionsInDfaDict[i]:
                    tempList2 = sorted(j[0:len(j) - 1])
                    tempList2 += [j[len(j) - 1]]
                    if tempList2[0] == -1337:
                        del tempList2[0]
                    tempTuple = tuple(tempList2)
                    tempList.append(tempTuple)
                tempResult[i] = tempList
        return tempResult

    def __makeStates(self, tempResult: dict, dictOfPartitions: dict) -> dict:
        converted = {}
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
        return converted

    def __unnecessaryState(self, Dict: dict, start: State) -> int:
        for i in Dict:
            counter = 0
            for j in Dict:
                if Dict[i] == start:
                    counter = 1
                    break
                if j != i:
                    if i in Dict[j].transitions.values():
                        counter += 1
            if counter == 0:
                return i
        return -3

    def convertToDFA(self) -> DFA:
        allStates = self.__partitions()
        dictOfPartitions = self.__makeDictOfPartitions(allStates)
        dfaDict = self.__makeDFAdict(dictOfPartitions)
        mergedTransitionsInDfaDict = self.__mergeTransitions(dfaDict)
        mergedTransitionsInDfaDict = self.__simplify(mergedTransitionsInDfaDict)
        tempResult = self.__transitionsToTuples(mergedTransitionsInDfaDict)
        converted = self.__makeStates(tempResult, dictOfPartitions)

        help = sorted(self.allStatesUsingOnlyEpsilonEdges(self.__stateNumber(list(self.dictOfStates.keys())[0])))
        help.append(-2)
        startingNFAState = tuple(help)
        startingNFAState = dictOfPartitions[startingNFAState]
        startingNFAState = converted[startingNFAState]

        unnecessaryState = self.__unnecessaryState(converted, startingNFAState)
        while(unnecessaryState != -3):
            converted.pop(unnecessaryState)
            unnecessaryState = self.__unnecessaryState(converted, startingNFAState)

        finalDFA = DFA(converted, startingNFAState, self.alphabet)

        return finalDFA