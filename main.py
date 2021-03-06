from NFA import *

"""DFA EXAMPLE 1"""
"""
state0 = State(0, True, {0: 0, 1: 1})
state1 = State(1, True, {0: 4, 1: 2})
state2 = State(2, True, {0: 2, 1: 3})
state3 = State(3, False, {0: 3, 1: 3})
state4 = State(4, True, {0: 1, 1: 3})

list = {0: state0, 1: state1, 2: state2, 3: state3, 4: state4}

alphabet = [0, 1] #[0, 1, 2]
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
"""END OF EXAMPLE 1"""
#---------------------------------------------------------------------------#
"""EXAMPLE 2 """
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
    print("Accepts")
else:
    print("Doesn't accept")
"""
"""END OF EXAMPLE 2"""
#-----------------------------------------------------------------------------
"""CONVERT NFA TO DFA EXAMPLE"""
"""
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
str5 = "010"
alphabet = [1, 0]
states = {0: state0, 1: state1, 2: state2, 3: state3, 4: state4, 5: state5, 6: state6, 99: state99}
nfa = NFA(states, state0, alphabet)
dfa = nfa.convertToDFA()
print(dfa.accepts(str5))
"""

"""NFA TO DFA IZ TEKE"""
"""
alfabet = ['a', 'b']
state1 = State(0, False, {'a':  [2], "epsilon": [1]})
state2 = State(1, True, {'a': [0]})
state3 = State(2, False, {'a': [1], 'b': [1, 2]})
states = {0: state1, 1: state2, 2: state3}
nfa2 = NFA(states, state1, alfabet)
string123 = "baa"
if(nfa2.accepts(string123)):
    print("Accepts")
else:
    print("Doesn't accept")

dfa2 = nfa2.convertToDFA()
if(dfa2.accepts(string123)):
    print("Accepts")
else:
    print("Doesn't accept")
"""

"""
#a* + (ab)*
alfabet = ['a', 'b']
state0 = State(0, False, {"epsilon": [1, 2]})
state1 = State(1, True, {'a': [1]})
state2 = State(2, False, {'a': [3]})
state3 = State(3, False, {'b': [4]})
state4 = State(4, True, {"epsilon": [2]})
states = {0: state0, 1: state1, 2: state2, 3: state3, 4: state4}
nfa = NFA(states, state0, alfabet)
if nfa.accepts("abababababab"):
    print("Accepts")
else:
    print("Doesn't accept")
"""

"""
#NFA that accepts all binary strings that end with 101
alfabet = [0, 1]
state0 = State(0, False, {0: [0], 1: [0, 1]})
state1 = State(1, False, {0: [2]})
state2 = State(2, False, {1: [3]})
state3 = State(3, True, {})
states = {0: state0, 1: state1, 2: state2, 3: state3}
nfa = NFA(states, state0, alfabet)
dfa = nfa.convertToDFA()
if nfa.accepts("0100111"):
    print("Accepts")
else:
    print("Doesn't accept")
"""

"""
#Accepts all binary strings where the last symbol is 0 or that contain only 1’s
alfabet = [0, 1]
state0 = State(0, True, {1: [0]})
state1 = State(1, False, {"epsilon": [0, 2]})
state2 = State(2, False, {0: [2, 3], 1: [2]})
state3 = State(3, True, {})
states = {0: state0, 1: state1, 2: state2, 3: state3}
nfa = NFA(states, state1, alfabet)
if nfa.accepts("1011"):
    print("Accepts")
else:
    print("Doesn't accept")
"""