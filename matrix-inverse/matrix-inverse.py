import numpy as np
from numpy import linalg as LA
def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.array(A)
    dim = A.ndim
    x, y = A.shape
    det = LA.det(A)
    
    if not (dim == 2 and x == y and det != 0):
        return None

    return LA.inv(np.array(A))
