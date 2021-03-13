# -*- coding: utf-8 -*-
"""...
"""
import numpy as np
import numpy.ma as ma


def hadamard(n):
    H = np.array([[True]], dtype='?')
    for i in range(0, n):
        H = np.block([[H, H], [H, ~H]])
    return H


def main():
    # x = [0, 1, 0]
    # b = np.array(x, dtype='?')
    m = hadamard(1)
    data = np.array([[1, 2], [3, 4]])
    print(data)
    masked = ma.masked_array(data, mask=~m)
    print(masked)
    return


if __name__ == '__main__':
    main()
    print('\ndone')
