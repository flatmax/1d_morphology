import numpy as np

try:
    from .dilation import dilation
    from .erosion import erosion
except ImportError:
    from dilation import dilation
    from erosion import erosion


def opening(f, g):
    """
    open = opening(f, g)
    erosion followed by dilation
    
    NB: this works for set or function definitions
    
    Ref: Morphology.lyx, May 2020
    """
    f = np.asarray(f).flatten()
    open_result = dilation(erosion(f, g), g)
    
    return open_result
