import numpy as np
from dilation import dilation
from erosion import erosion


def closing(f, g):
    """
    close = closing(f, g)
    dilation followed by erosion
    
    NB: this works for set or function definitions
    
    Ref: Morphology.lyx, May 2020
    """
    f = np.asarray(f).flatten()
    close = erosion(dilation(f, g), g)
    
    return close
