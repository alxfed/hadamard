# -*- coding: utf-8 -*-
"""...
"""
import numpy as np
from scipy.linalg import hadamard


def main():
    data = [1, 2, 3, 4]
    # data_m = np.array([data,] * len(data))
    # more literate
    data_a = np.array(data)
    data_m = np.tile(data_a, (4, 1))
    h4 = hadamard(4, dtype=int)
    trans = data_m * h4
    print(trans)
    return


if __name__ == '__main__':
    main()
    print('\ndone')
