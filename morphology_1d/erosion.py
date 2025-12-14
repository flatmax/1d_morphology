import numpy as np
from scipy.ndimage import minimum_filter1d


def erosion(f, g):
    """
    eros = erosion(f, g)
    This calculates the EROSION of function f by either
    a structuring function g or a set
    
    NB1: If all elements of g are the same, this calculates the erosion of f by a set
         OR if length(g)==1 this also calculates the dilation of f by a set
    NB2: The output is aligned with the original signal
    
    Ref: Morphology.lyx, Section 2
    """
    f = np.asarray(f).flatten()
    g = np.asarray(g).flatten()
    
    N = len(f)
    B = len(g)
    Bhalf = B // 2
    
    if (B == 1) or (np.max(g) == np.min(g)):
        # use set definitions
        # origin=0 centers the filter at index B//2
        eros = minimum_filter1d(f, size=B, mode='nearest', origin=0)
    else:
        # use function definitions
        if B % 2 == 0:
            raise ValueError('Length of structuring element must be an odd number for function definitions')
        Bhalf = (B - 1) // 2
        eros = np.zeros(N)
        for n in range(N):
            if n < Bhalf:
                fn = f[0:n + Bhalf + 1]
                gn = g[Bhalf + n::-1]
            elif n > N - Bhalf - 1:
                fn = f[n - Bhalf:N]
                g_flipped = np.flip(g)
                gn = g_flipped[0:len(fn)]
            else:
                fn = f[n - Bhalf:n + Bhalf + 1]
                g_flipped = np.flip(g)
                gn = g_flipped[0:len(fn)]
            eros[n] = np.min(fn - gn)
    
    return eros
