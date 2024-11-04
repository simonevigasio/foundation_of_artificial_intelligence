# Enable the filesystem to access the parent directory.
import sys
sys.path.append('../')

# Import essential classes and functions required to work with the search problem.
from init import *

# Implement the breadth-first search algorithm.
def breadth_first_search(problem):
  """Searches the shallowest nodes in the search tree first."""

  # Initialize the initial node and check if it is already the goal state.
  node = Node(problem.initial)
  if problem.is_goal(problem.initial):
      return node

  # Initialize the frontier using a FIFO queue and add the initial node.
  frontier = FIFOQueue([node])
  reached = { problem.initial }

  # Continue the search loop until the frontier is empty.
  while frontier:

    # Remove the first node from the queue (FIFO behavior).
    node = frontier.pop()

    # Expand the node to generate its children.
    for child in node.expand(problem):
      s = child.state

      # Check if the child node is the goal state.
      if problem.is_goal(s):
       return child

      # If the child node's state is new, add it to the frontier and mark as reached.
      if s not in reached:
        reached.add(s)
        frontier.appendleft(child)

  # Return a failure result if no goal state was found.
  return failure