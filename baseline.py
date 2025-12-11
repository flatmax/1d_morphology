import numpy as np

try:
    from .opening import opening
    from .closing import closing
except ImportError:
    from opening import opening
    from closing import closing


def baseline(f, g=None):
    """
    baseline = baseline(f, g)
    
    NB: this works for set or function definitions
    
    Ref: Morphology.lyx, May 2020
    """
    if g is None:
        try:
            from .structfunct import structfunct
        except ImportError:
            from structfunct import structfunct
        g = structfunct(11, 'quad')
    
    f = np.asarray(f).flatten()
    
    open_result = opening(f, g)    # erosion, then dilation
    close_result = closing(f, g)   # dilation, then erosion
    
    baseline_result = (open_result + close_result) / 2
    
    return baseline_result
