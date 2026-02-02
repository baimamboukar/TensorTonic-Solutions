import numpy as np
from numpy import linalg as LA

def manhattan_distance(x, y) -> float:
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)

    return LA.norm(x - y, ord=1)