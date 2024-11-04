# Enable the filesystem to access the parent directory and specific subdirectories.
import sys
sys.path.append('../')  # Add the parent directory to the system path to allow importing modules from it.

# Import the best-first search algorithm from the specified module.
from best_first_search import *  # Import the best-first search function to use in implementing greedy best-first search.

# Define the greedy best-first search function.
def greedy_bfs(problem, h=None):
    """
    Perform a greedy best-first search on the given problem.
    
    Args:
        problem: The search problem to solve, which includes the initial state and goal test.
        h: A heuristic function that takes a node and returns an estimate of the cost to reach the goal.
           If not provided, it defaults to the heuristic defined in the problem.
           
    Returns:
        The goal node if found, or 'failure' if no solution exists.
    """
    # Use the provided heuristic function h or default to the problem's heuristic.
    h = h or problem.h  # If no heuristic is provided, use the default heuristic defined in the problem.
    
    # Use the best-first search algorithm, passing the heuristic function h as the evaluation function.
    return best_first_search(problem, f=h)