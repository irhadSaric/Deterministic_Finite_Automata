class State:
    def __init__(self, stateNumber: int, isFinalState: bool, transitions: dict):
        self.stateNumber = stateNumber
        self.isFinalState = isFinalState
        self.transitions = transitions
