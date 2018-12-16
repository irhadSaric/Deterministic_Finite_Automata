from DFA import *

state0 = State(0, 0, 1, True, None)
state1 = State(1, 4, 2, True, None)
state2 = State(2, 2, 3, True, None)
state3 = State(3, 3, 3, False, None)
state4 = State(4, 1, 3, True, None)

list = []
list.append(state0)
list.append(state1)
list.append(state2)
list.append(state3)
list.append(state4)

str1 = "000100"
str2 = "1111"

dfa = DFA(list, state0)

if dfa.accepts(str1):
    print("Accepts str1")
if dfa.accepts(str2):
    print("Accepts str2")
