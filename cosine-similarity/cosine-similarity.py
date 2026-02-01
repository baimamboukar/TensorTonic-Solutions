import numpy as np
from numpy import linalg as LA

def cosine_similarity(a, b) -> float:
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)

    normA = LA.norm(a)
    normB = LA.norm(b)

    if normA == 0 or normB == 0:
        return 0

    return float(np.dot(a, b) / (normA * normB))