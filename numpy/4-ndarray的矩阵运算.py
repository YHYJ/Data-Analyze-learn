# -*- coding: utf-8 -*-

"""
Date: 2018-01-18 16:51:47
Last modified: 2018-01-18 16:51:47
Author: YJ1516 - yj1516268@outlook.com

"""

import numpy as np


arr1 = np.arange(1, 6)        # [1 2 3 4 5]
arr2 = np.arange(10, 51, 10)  # [10 20 30 40 50]

# 1.数组之间的运算
print(arr1 + arr2)
print(arr1 * arr2)

# 2.数组和数字之间的运算
print(arr1 + 20)
print(arr2 / 2)

# 3.多维数组和多维数组之间的运算
arr3 = np.arange(9).reshape((3, 3))
arr4 = np.arange(9).reshape((3, 3))
print(arr3 + arr4)

# 4.一维数组和多维数组之间的运算
arr5 = np.arange(5)     # [0 1 2 3 4]
arr6 = np.arange(10).reshape((2, 5))    # [[0 1 2 3 4] [5 6 7 8 9]]
print(arr5 + arr6)      # [[0 2 4 6 8] [5 7 9 11 13]]
