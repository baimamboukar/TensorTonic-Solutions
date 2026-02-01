import numpy as np

def dot_product(x, y) -> flaot:
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    
    x = np.array(x)
    y = np.array(y)
    
    if (x.shape != y.shape):
        raise ValueError("X and Y mismatch")

    return float(np.dot(x, y))