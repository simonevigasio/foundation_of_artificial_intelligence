# Enable the filesystem to access the parent directory and specific subdirectories.
import sys
sys.path.append('../')  # Add the parent directory to the system path for module imports.

from backtracking_search import *

# This is a constraint satisfation problem, where we have seven variable each one representing a state.
# We wound like to assign to each state a color between (0) red, (1) blue, (2) green. 
# There are some states that are neighbours to each other, and we don't want that neighbour states have same colors.
# Propose a possible solution: 

# Array of all the possible colors that each state can have {0: red, 1: blue, 2: green}.
domains = [
    (0, 1, 2), # state 0
    (0, 1, 2), # state 1
    (0, 1, 2), # state 2
    (0, 1, 2), # state 3
    (0, 1, 2), # state 4
    (0, 1, 2), # state 5
    (0, 1, 2)  # state 6
]

# Matrix used to represent all the possible not wanted couples of value within the assignment of colors.
constraints = [
    # this row is representing the state 0 respect to all other states
    [
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 0 is near to the state 1 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 0 is near to the state 2 => we don't want the they have the same colors
        [], 
        [], 
        [], 
        []
    ],

    # this row is representing the state 1 respect to all other states
    [
        [(0, 0), (1, 1), (2, 2)], # the state 1 is near to the state 0 => we don't want the they have the same colors
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 1 is near to the state 2 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 1 is near to the state 3 => we don't want the they have the same colors
        [], 
        [], 
        []
    ],

    # this row is representing the state 2 respect to all other states
    [
        [(0, 0), (1, 1), (2, 2)], # the state 2 is near to the state 0 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 2 is near to the state 1 => we don't want the they have the same colors
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 2 is near to the state 3 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 2 is near to the state 4 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 2 is near to the state 5 => we don't want the they have the same colors
        []
    ],

    # this row is representing the state 3 respect to all other states
    [
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 3 is near to the state 1 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 3 is near to the state 2 => we don't want the they have the same colors
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 3 is near to the state 4 => we don't want the they have the same colors
        [], 
        []
    ],

    # this row is representing the state 4 respect to all other states
    [
        [], 
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 4 is near to the state 2 => we don't want the they have the same colors
        [(0, 0), (1, 1), (2, 2)], # the state 4 is near to the state 3 => we don't want the they have the same colors
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 4 is near to the state 5 => we don't want the they have the same colors
        []
    ],

    # this row is representing the state 5 respect to all other states
    [
        [], 
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 5 is near to the state 2 => we don't want the they have the same colors
        [], 
        [(0, 0), (1, 1), (2, 2)], # the state 5 is near to the state 4 => we don't want the they have the same colors
        [], 
        []
    ],

    # this row is representing the state 6 respect to all other states
    [
        [], 
        [],
        [], 
        [], 
        [], 
        [], 
        []
    ],
]

# Initialization of the problem with domain and constraints.
map_color_csp = CSP(domains=domains, constraints=constraints)

# Get the result from the backtracking algorithm.
res = backtracking_search(map_color_csp)

# Print the result.
print(res)