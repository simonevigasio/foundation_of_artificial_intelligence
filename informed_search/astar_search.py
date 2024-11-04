# Enable the filesystem to access the parent directory and specific subdirectories.
import sys
sys.path.append('../')  # Add the parent directory to the system path to allow importing modules from it.

# Import the best-first search algorithm from the specified module.
from best_first_search import *  # Import all relevant functions and classes needed for search algorithms.

# Define the cost function g for the path cost from the root to a given node.
def g(n):
    """
    Return the path cost of a given node.
    
    Args:
        n: A Node object representing a state in the search tree.
        
    Returns:
        The path cost from the initial state to the node.
    """
    return n.path_cost  # Return the cumulative path cost from the root to the current node.

# Define the A* search algorithm.
def astar_search(problem, h=None):
    """
    Perform an A* search on the given problem.
    
    Args:
        problem: The search problem to solve, which includes the initial state and goal test.
        h: A heuristic function that estimates the cost to reach the goal from a node.
           If not provided, it defaults to the heuristic defined in the problem.
           
    Returns:
        The goal node if found, or 'failure' if no solution exists.
    """
    h = h or problem.h  # Use the provided heuristic or default to the problem's heuristic if none is given.
    
    # Use the best-first search with the evaluation function f(n) = g(n) + h(n).
    return best_first_search(problem, f=lambda n: g(n) + h(n))

# Define the weighted A* search algorithm.
def weighted_astar_search(problem, h=None, weight=1.4):
    """
    Perform a weighted A* search on the given problem.
    
    Args:
        problem: The search problem to solve, which includes the initial state and goal test.
        h: A heuristic function that estimates the cost to reach the goal from a node.
           If not provided, it defaults to the heuristic defined in the problem.
        weight: A multiplier for the heuristic to emphasize its influence on the search.
        
    Returns:
        The goal node if found, or 'failure' if no solution exists.
    """
    h = h or problem.h  # Use the provided heuristic or default to the problem's heuristic if none is given.
    
    # Use the best-first search with the evaluation function f(n) = g(n) + weight * h(n).
    return best_first_search(problem, f=lambda n: g(n) + weight * h(n))