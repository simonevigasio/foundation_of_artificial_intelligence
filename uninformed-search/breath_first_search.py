import sys
sys.path.append('../')

from search_problem_init import *

def breadth_first_search(problem):
  """Search shallowest nodes in the search tree first"""
  node = Node(problem.initial)
  if problem.is_goal(problem.initial):
    return node
  frontier = FIFOQueue([node])
  reached = {problem.initial}
  while frontier:
    node = frontier.pop()
    for child in node.expand(problem):
      s = child.state
      if problem.is_goal(s):
        return child
      if s not in reached:
        reached.add(s)
        frontier.appendleft(child)
  return failure