import math

class Problem(object):
  """Represents the definition of a search problem."""

  def __init__(self, initial=None, goal=None):
    """Initialize a Problem instance with an initial state and a goal state."""
    self.initial = initial
    self.goal = goal

  # Define the set of actions available from a given state (to be implemented in subclasses)
  def actions(self, state): raise NotImplementedError

  # Define the result of applying an action to a given state (to be implemented in subclasses)
  def result(self, state, action): raise NotImplementedError

  # Check if the given state is the goal state
  def is_goal(self, state): return state == self.goal

  # Calculate the cost of performing an action from state `s` to `s1` (default is 1)
  def action_cost(self, s, a, s1): return 1

  # Heuristic function for informed search (default returns 0)
  def h(self, node): return 0

class Node():
  """Represents a node in a search tree."""

  def __init__(self, state, parent=None, action=None, path_cost=0):
    """Create a Node that represents a state in the search tree, derived from a parent node."""
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost
    self.depth = 0  # Depth of the node in the tree

    # If the node has a parent, increment the depth based on the parent's depth
    if parent:
      self.depth = parent.depth + 1

  # Calculate the length of the path from the root to this node
  def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))

  # Handle Node with the same value in the Priority Queue
  def __lt__(self, other): return self.path_cost < other.path_cost

  def expand(self, problem):
    """Generate all child nodes reachable in one step from this node."""
    return [self.child_node(problem, action) for action in problem.actions(self.state)]

  def child_node(self, problem, action):
    """Create a new child node resulting from applying an action to the current node."""
    next_state = problem.result(self.state, action)
    next_node = Node(
        next_state, self, action,
        self.path_cost + problem.action_cost(self.state, action, next_state)
    )
    return next_node

# Define special nodes to represent failure or cutoff conditions
failure = Node('failure', path_cost=math.inf)
cutoff = Node('cutoff', path_cost=math.inf)

# Import deque from collections for FIFO queue implementation
from collections import deque
FIFOQueue = deque  # Queue following First-In-First-Out behavior
LIFOQueue = list   # Queue following Last-In-First-Out behavior (stack)

import heapq
class PriorityQueue():
  """A priority queue where the item with the minimum f(item) value is popped first."""

  def __init__(self, items=(), key=lambda x: x):
    """Initialize a priority queue with a given scoring function and initial items."""
    self.key = key
    self.items = []
    for item in items:
      self.add(item)

  def add(self, item):
    """Add an item to the priority queue."""
    heapq.heappush(self.items, (self.key(item), item))

  def pop(self):
    """Remove and return the item with the minimum f(item) value."""
    return heapq.heappop(self.items)[1]
  
# Define the class used for solving Constraint Satisfation Problems
class CSP():
  """Constraint Satisfation Problem."""

  def __init__(self, domains=[], constraints=[]):
    """
    Initialization of the problem.

    Args: 
      domains: array of tuples contrining the values of each variable
      constraints: matrix of arrays contrainig tuples of not accepted couple values
      initial: initial state of the assignments
      failure: case where a solution is not reachable
    """
    self.domains = domains
    self.constraints = constraints
    self.initial = [None] * len(domains)
    self.failure = [None] * len(domains)

  def is_goal(self, assignment): # miss further checking
    """Check whether the assignment is a possible goal."""
    for var in assignment:
      if var is None:
        return False
    return True 

  def select_unassigned_variable(self, assignment): 
    """Select the first variable without a value into the assignment."""
    for var in range(len(assignment)): 
      if assignment[var] is None: 
        return var

  def order_domain_values(self, var, assignment): 
    """Receive all the values in the domain of the givem variable."""
    return self.domains[var]

  def is_consistent(self, var, value, assignment): 
    """Check the validity of the assignment given the new value."""
    if value not in self.domains[var]: return False
    dim = len(self.domains)
    for i in range(dim):
      for t1 in self.constraints[var][i]:
        if t1[0] == value and t1[1] == assignment[i]: 
          return False
      for t2 in self.constraints[i][var]:
        if t2[0] == assignment[i] and t2[1] == value:
          return False
    return True 

  def add_value(self, var, value, assignment): 
    """Add to the assignment the given value to the given variable."""
    assignment[var] = value

  def remove_value(self, var, assignment): 
    """Remove the value from the given variable."""
    assignment[var] = None