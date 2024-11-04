# Import essential classes and functions for the search algorithm.
from search_problem_init import Node, PriorityQueue, failure  # Import the Node class, PriorityQueue for managing the frontier, and failure constant.

def best_first_search(problem, f):
    """
    Perform a best-first search algorithm on a given problem.
    
    Args:
        problem: The search problem to solve, which includes the initial state and goal test.
        f: A function that takes a node and returns its evaluation value, guiding the search.
        
    Returns:
        The goal node if found, or 'failure' if no solution exists.
    """
    
    # Initialize the root node with the initial state of the problem.
    node = Node(problem.initial)
    
    # Initialize the frontier as a priority queue ordered by the function f.
    frontier = PriorityQueue([node], key=f)
    
    # Dictionary to keep track of reached states and their associated nodes.
    reached = { problem.initial: node }
    
    # Loop until the frontier is empty (all nodes have been expanded).
    while frontier:
        # Remove and return the node with the lowest f value from the frontier.
        node = frontier.pop()
        
        # Check if the current node's state is the goal state.
        if problem.is_goal(node.state):
            return node  # Return the goal node if found.
        
        # Expand the current node to generate its child nodes.
        for child in node.expand(problem):
            s = child.state  # Get the state of the child node.
            
            # Check if the state is new or if a better path to this state is found.
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child  # Update the reached dictionary with the new or better node.
                frontier.add(child)  # Add the child node to the frontier.
    
    # Return failure if no solution is found after exploring all nodes.
    return failure