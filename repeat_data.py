# -*- coding: utf-8 -*-
"""...
"""
import numpy as np
# from scipy.linalg import hadamard


def hadamard_old(n):
    """
    # Sylvester construction
    :param n: (divisible by 2)
    :return: h
    """
    H = np.array([[1]], dtype=int)
    for i in range(0, n):
        H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))
    return H


def hadamard(n):
    H = np.array([[1]], dtype=int)
    for i in range(0, n):
        H = np.block([[H, H], [H, -H]])
    return H


def main():
    data = [1, 2, 3, 4]
    # data_m = np.array([data,] * len(data))
    # more literate
    data_a = np.array(data)
    data_3 = np.broadcast_to(array=data_a, shape=(4,4,4,4))
    data_m = np.tile(data_a, (4, 1))
    h4 = hadamard(2)
    trans = data_m * h4
    print(trans)
    return


if __name__ == '__main__':
    main()
    print('\ndone')
