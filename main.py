from NFA import *

"""
    Malekov komentar
"""

"""
state0 = State(0, True, {0: 0, 1: 1})
state1 = State(1, True, {0: 4, 1: 2})
state2 = State(2, True, {0: 2, 1: 3})
state3 = State(3, False, {0: 3, 1: 3})
state4 = State(4, True, {0: 1, 1: 3})

#????????????????????
list = []
list.append(state0)
list.append(state1)
list.append(state2)
list.append(state3)
list.append(state4)

alphabet = [0, 1]
str1 = "000100"
str2 = "1111"

dfa = DFA(list, state0, alphabet)

if dfa.accepts(str1):
    print("Accepts str1")
else:
    print("Doesn't accept str1")
if dfa.accepts(str2):
    print("Accepts str2")
else:
    print("Doesn't accept str2")

"""

"""
state0 = State(0, False, {'i': 1, 'r': 5, 'h': 5, 'o': 5})
state1 = State(1, False, {'i': 5, 'r': 2, 'h': 5, 'o': 5})
state2 = State(2, False, {'i': 5, 'r': 5, 'h': 3, 'o': 5})
state3 = State(3, False, {'i': 5, 'r': 5, 'h': 5, 'o': 4})
state4 = State(4, True, {'i': 4, 'r': 4, 'h': 4, 'o': 4})
state5 = State(5, False, {'i': 5, 'r': 5, 'h': 5, 'o': 5})

states = {0: state0, 1: state1, 2: state2, 3: state3, 4: state4, 5: state5}
str3 = "irhoirho"
alphabet = ['i', 'r', 'h', 'o']
dfa = DFA(states, state0, alphabet)

if dfa.accepts(str3):
    print("Prihvata")
else:
    print("Ne prihvata")
"""
"""TEST ZA NFA KONVERT
state0 = State(0, False, {1: [1, 5], "epsilon": [99]})
state1 = State(1, False, {0: [2, 99], 1: [3]})
state2 = State(2, False, {})
state3 = State(3, False, {1: [4], "epsilon": [1]})
state4 = State(4, True, {})
state5 = State(5, False, {0: [6]})
state6 = State(6, True, {1: [6]})
state99 = State(99, True, {0: [99], "epsilon": [2, 3]})

str = "11101"
str2 = "111"
str3 = "101111111"
str4 = "0000000"
alphabet = [1, 0]
states = {0: state0, 1: state1, 2: state2, 3: state3, 4: state4, 5: state5, 6: state6, 99: state99}
nfa = NFA(states, state0, alphabet)
dfa = nfa.convertToDFA()
print(dfa.accepts("111"))
#nfa.allStatesUsingOnlyEpsilonEdges(state0)
"""

"""
if nfa.accepts(str4):
    print("Prihvata")
else:
    print("Ne prihvata")
"""
"""
for j in range (1, 5):
    for i in combinations(states.keys(), j):
        for k in range (0, len(i)):
            print(i[k], end=" ")
        print()
#print(combinations("01234", 2), end=" ")
#print(combinations("01234", 3), end=" ")
"""

"""NFA TO DFA IZ TEKE"""
alfabet = ['a', 'b']
state1 = State(1, False, {'a':  [3], "epsilon": [2]})
state2 = State(2, True, {'a': [1]})
state3 = State(3, False, {'a': [2], 'b': [2, 3]})
states = {1: state1, 2: state2, 3: state3}
nfa2 = NFA(states, state1, alfabet)
string123 = "aba"
if(nfa2.accepts(string123)):
    print("Prihvata")
else:
    print("Ne prihvata")

dfa2 = nfa2.convertToDFA()
if(dfa2.accepts(string123)):
    print("Prihvata")
else:
    print("Ne prihvata")