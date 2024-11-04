# Enable the filesystem to access the parent directory for module imports.
import sys
sys.path.append('../')  # Add the parent directory to the system path to allow importing modules located there.

# Import the best-first search algorithm from the specified module.
from best_first_search import *  # Import the best-first search function to use in implementing uniform-cost search.

# Define the cost function g for uniform-cost search.
def g(n):
    """
    Return the path cost of a given node.
    
    Args:
        n: A Node object representing a state in the search tree.
        
    Returns:
        The path cost from the initial state to the node.
    """
    return n.path_cost  # Return the cumulative cost associated with the path to this node.

# Implement the uniform-cost search algorithm.
def uniform_cost_search(problem):
    """
    Perform a uniform-cost search on the given problem.
    
    Args:
        problem: The search problem to solve, which includes the initial state and goal test.
        
    Returns:
        The goal node if found, or 'failure' if no solution exists.
    """
    # Use the best-first search algorithm with the cost function g to prioritize nodes with the lowest path cost.
    return best_first_search(problem, f=g)