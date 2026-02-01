import numpy as np

def matrix_trace(A) -> int:
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """

    trace = 0
    A = np.array(A)
    n, m = A.shape


    for i in range(n):
            trace += A[i,i]
    
    return trace
