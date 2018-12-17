from State import State

class DFA:
    def __init__(self):
        self.dictOfStates = {}
        self.startingState = None
        self.alphabet = []

    def __init__(self, dictOfStates : dict, startingState : State, alphabet: list):
        self.dictOfStates = dictOfStates
        self.startingState = startingState
        for i in alphabet:
            for key, value in dictOfStates.items():
                if i not in value.transitions:
                    print("Missing transition for " + str(i) + ", state: ", key)
                    return
        self.alphabet = alphabet

    def __getStateUsingStateNumber(self, number: int):
        for state in self.listOfStates:
            if state.stateNumber == number:
                return state

    def __stateNumber(self, number: int) -> State:
        for state in self.listOfStates:
            if state.stateNumber == number:
                return state

    def accepts(self, string: str) -> bool:
        currentState = self.startingState
        for i in string:
            if not i.isalpha():
                nextState = currentState.transitions[int(i)]
            else:
                nextState = currentState.transitions[i]
            currentState = self.dictOfStates[nextState]
            #print(currentState.stateNumber)
        if currentState.isFinalState :
            return True
        else:
            return False