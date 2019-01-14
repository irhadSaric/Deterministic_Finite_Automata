from State import State

class DFA(object):
    def __init__(self):
        self.dictOfStates = {}
        self.startingState = None
        self.alphabet = []

    def __init__(self, dictOfStates: dict, startingState: State, alphabet: list):
        self.dictOfStates = dictOfStates
        self.startingState = startingState
        self.alphabet = alphabet

    def __getStateUsingStateNumber(self, number: int):
        for state in self.dictOfStates:
            if state.stateNumber == number:
                return state

    """def __stateNumber(self, number: int) -> State:
        for state in self.listOfStates:
            if state.stateNumber == number:
                return state"""

    def accepts(self, string: str) -> bool:
        try:
            for i in self.alphabet:
                for key, value in self.dictOfStates.items():
                    if i not in value.transitions:
                        raise Exception("ERROR : Missing transition: state-> " + str(key) + ", symbol-> " + str(i))
                        return False

            currentState = self.startingState
            for i in string:
                if not i.isalpha():
                    nextState = currentState.transitions[int(i)]
                else:
                    nextState = currentState.transitions[i]
                currentState = self.dictOfStates[nextState]
                #print(currentState.stateNumber)
            if currentState.isFinalState:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False