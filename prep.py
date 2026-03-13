import numpy as np
from scipy.stats import unitary_group

def build_U(N):
    """
    Build U as a random unitary matrix of size N x N, 
    sampled from the Haar measure.
    """
    return unitary_group.rvs(N)

def build_O(N):
    """
    O is defined using the Stornati et al definition:

        O ∈ Sp2N,R ∩ SO(2N) ≅ U(N) 
    
    which represents a passive transformation that commutes with the 
    operator n = a†a.

    Is a 2N x 2 symplectic orthogonal matrix that acts as a passive optical linear network.
    So:

        O = [[Re(U), -Im(U)],
             [Im(U), Re(U)]]

    where U is the N x N unitary matrix that represents the transformation.
    """
    U = build_U(N)
    return np.block([[np.real(U), -np.imag(U)], [np.imag(U), np.real(U)]])
