# -*- coding: utf-8 -*-
"""...
"""
import numpy as np


def hadamard(n):
    H1 = np.array([[1, 1], [1, -1]], dtype=int)
    H = H1
    for i in range(1, n):
        H = np.kron(H1, H)
    return H


def main():
    print(hadamard(2))
    return


if __name__ == '__main__':
    main()
    print('\ndone')
