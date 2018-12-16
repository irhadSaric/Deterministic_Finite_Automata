from State import State

class DFA:
    def __init__(self):
        self.listOfStates = []
        self.startingState = None

    def __init__(self, listOfStates : list, startingState : State):
        self.listOfStates = listOfStates
        self.startingState = startingState

    def __stateNumber(self, number: int) -> State:
        for state in self.listOfStates:
            if state.stateNumber == number:
                return state

    def accepts(self, string: str) -> bool:
        currentState = self.startingState
        for i in string:
            if int(i) == 0:
                nextState = currentState.stateFor0
            elif int(i) == 1:
                nextState = currentState.stateFor1
            currentState = self.__stateNumber(nextState)
            print(currentState.stateNumber)
        if currentState.isFinalState :
            return True
        else:
            return False