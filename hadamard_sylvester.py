# -*- coding: utf-8 -*-
"""...
"""
import numpy as np


def hadamard(n): # n is the order of Sylvester construction, not the dimension of the matrix as the idiots did it.
    H = np.array([[1]], dtype=int)
    for i in range(0, n):
        H = np.block([[H, H], [H, -H]])
    return H

def main():
    print(hadamard(2))
    return


if __name__ == '__main__':
    main()
    print('\ndone')
