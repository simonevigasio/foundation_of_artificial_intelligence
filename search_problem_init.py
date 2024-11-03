import math

class Problem(object):
  """Problem definition"""

  def __init__(self, initial=None, goal=None):
    """Create a Problem instance, given an initial state and a goal state"""
    self.initial = initial
    self.goal = goal

  def actions(self, state): raise NotImplementedError
  def result(self, state, action): raise NotImplementedError
  def is_goal(self, state): return state == self.goal
  def action_cost(self, s, a, s1): return 1
  def h(self, node): return 0

class Node():
  """A Node in a search tree"""

  def __init__(self, state, parent=None, action=None, path_cost=0):
    """Create a search tree Node, derived from a parent by an action"""
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost
    self.depth = 0
    if parent:
      self.depth = parent.depth + 1

  def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))

  def expand(self, problem):
    """List the nodes reachable in one step from this node"""
    return  [self.child_node(problem, action) for action in problem.actions(self.state)]

  def child_node(self, problem, action):
    """Given an action, visualize the next node of the search tree"""
    next_state = problem.result(self.state, action)
    next_node = next_node = Node(next_state, self, action, self.path_cost + problem.action_cost(self.state, action, next_state))
    return next_node
  
failure = Node('failure', path_cost=math.inf)
cutoff = Node('cutoff', path_cost=math.inf)
  
from collections import deque
FIFOQueue = deque # First-in First-out Queue
LIFOQueue = list # Last-in First-out Queue

import heapq # Heap data structure
class PriorityQueue():
  """A queue in which the item with minimum f(item) is always popped first"""

  def __init__(self, items=(), key=lambda x: x):
    """Create the priority queue given a score function key, and a set of items"""
    self.key = key # function for finding the score given the item
    self.items = [] # a heap of (score, item) pairs
    for item in items:
      self.add(item)

  def add(self, item):
    """Add item to the queue"""
    pair = (self.key(item), item)
    heapq.heappush(self.items, pair)

  def pop(self):
    """Pop and return the item with min f(item) value"""
    return heapq.heappop(self.items)[1]