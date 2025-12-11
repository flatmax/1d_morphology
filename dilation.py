import numpy as np
from scipy.ndimage import maximum_filter1d


def dilation(f, g):
    """
    dil = dilation(f, g)
    This calculates the DILATION of function f by either
    a structuring function g or a set
    
    NB1: If all elements of g are the same, this calculates the dilation of f by a set
         OR if length(g)==1 this also calculates the dilation of f by a set
    NB2: The output is aligned with the original signal
    
    Ref: Morphology.lyx, Section 2
    """
    f = np.asarray(f).flatten()
    g = np.asarray(g).flatten()
    
    N = len(f)
    B = len(g)
    Bhalf = (B - 1) // 2
    
    if B % 2 == 0:
        raise ValueError('Length of structuring element must be an odd number')
    
    if (B == 1) or (np.max(g) == np.min(g)):
        # use set definitions
        dil = maximum_filter1d(f, size=B, mode='nearest')
    else:
        # use function definitions
        dil = np.zeros(N)
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
                gn = g_flipped
            dil[n] = np.max(fn + gn)
    
    return dil
