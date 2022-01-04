# import neural_nets as nn
import numpy as np
#test rectified_linear_unit
def rectified_linear_unit(x):
    """ Returns the ReLU of x, or the maximum between 0 and x."""
    if x > 0:
        return 1
    else:
        return 0
    return np.max([x,0])
    print (result)

print (rectified_linear_unit(3))