# Enable the filesystem to access the parent directory.
import sys
sys.path.append('../')  # Add the parent directory to the system path to allow the import of modules from it.

# Import essential classes and functions required to work with the search problem.
from search_algorithms.search_problem_init import cutoff, failure  # Import 'cutoff' and 'failure' indicators from the specified module.

# Retrieve the path of nodes starting from the one given as a parameter.
def path_states(node):
    """
    Returns the sequence of states from the root to the given node.
    
    Args:
        node: The current node whose path to the root is being traced.
        
    Returns:
        A list representing the path of states from the root to the given node.
    """
    
    # Check if the node is a special case (cutoff, failure, or None), indicating an invalid or terminating condition.
    if node in (cutoff, failure, None):
        return []  # Return an empty list to signify no valid path.
    
    # Recursively call path_states on the parent node and concatenate the current node's state.
    return path_states(node.parent) + [node.state]  # Build the path by appending the current node's state to the path from the root.