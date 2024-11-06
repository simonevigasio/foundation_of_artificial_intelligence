# Enable the filesystem to access the parent directory and specific subdirectories.
import sys
sys.path.append('../')  # Add the parent directory to the system path for module imports.

from backtracking_search import *

domains = [
    (0, 1, 2),
    (0, 1, 2),
    (0, 1, 2),
    (0, 1, 2),
    (0, 1, 2),
    (0, 1, 2),
    (0, 1, 2)
]

constraints = [
    [[], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [], [], [], []],
    [[(0, 0), (1, 1), (2, 2)], [], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [], [], []],
    [[(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], []],
    [[], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [], [(0, 0), (1, 1), (2, 2)], [], []],
    [[], [], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [], [(0, 0), (1, 1), (2, 2)], []],
    [[], [], [(0, 0), (1, 1), (2, 2)], [], [(0, 0), (1, 1), (2, 2)], [], []],
    [[], [], [], [], [], [], []],
]

map_color_csp = CSP(domains=domains, constraints=constraints)

res = backtracking_search(map_color_csp)

print(res)