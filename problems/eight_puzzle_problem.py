# Enable the filesystem to access the parent directory.
import sys
sys.path.append('../')
sys.path.append('../search_algorithms')

# Import essential classes and functions required to work with the search problem.
from search_algorithms.search_problem_init import Problem, Node, cutoff, failure

# Import uninformed search algorithms for resolving the problem.
from uninformed_search.breath_first_search import breadth_first_search
from uninformed_search.depth_first_search import depth_first_search_recursive, depth_first_search_iterative

class EightPuzzle(Problem):

  def __init__(self, initial, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
    self.initial = initial
    self.goal = goal

  def actions(self, state):
    # the state is considered as a tuple of length 9 --> 9 blicks with a blank one
    moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4, 6), (3, 1, 5, 7), (2, 4, 8), (3, 7), (4, 6, 8), (5, 7)) # there can I move the value from the index-position
    blank = state.index(0) # get the index of the value 0 into the tuple
    return moves[blank] # return the available moves in that index-positionù

  def result(self, state, action):
    s = list(state)
    blank = state.index(0)
    s[action], s[blank] = s[blank], s[action]
    return tuple(s)
  
def path_states(node):
  "The sequence of states to get to this node."
  if node in (cutoff, failure, None): return []
  return path_states(node.parent) + [node.state]

e1 = EightPuzzle((8, 6, 7, 2, 5, 4, 3, 0, 1))
for s in path_states(depth_first_search_iterative(e1)): print(s)
