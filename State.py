class State:
    def __init__(self, stateNumber: int, stateFor0: int, stateFor1: int, isFinalState: bool, stateForEpsilon : int):
        self.stateNumber = stateNumber
        self.isFinalState = isFinalState
        self.stateFor0 = stateFor0
        self.stateFor1 = stateFor1
        self.stateForEpsilon = None
