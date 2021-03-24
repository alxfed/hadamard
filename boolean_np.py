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
    eye = np.ones(shape=(2, 2), dtype='?')
    zer = np.zeros(shape=(2, 2), dtype='?')
    # x = [0, 1, 0]
    # b = np.array(x, dtype='?')
    m = hadamard(1)
    fun = np.logical_and(eye, m, out=zer, where=eye)  # where is really-really promising, better than masks...
    data = np.array([[1, 2], [3, 4]])
    other = np.arange(start=5, stop=9, step=1, dtype=int).reshape((2, 2))
    print(data)
    mul = np.multiply(other, m)
    print(mul)
    masked = ma.array(data, mask=~m)  # mask is True when something needs to be masked out
    print(masked)
    print(masked.mask)
    print(masked[~masked.mask])
    return


if __name__ == '__main__':
    main()
    print('\ndone')
