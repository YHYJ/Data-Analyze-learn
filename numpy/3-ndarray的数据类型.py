# -*- coding: utf-8 -*-

"""
Date: 2018-01-18 16:32:10
Last modified: 2018-01-18 16:32:10
Author: YJ1516 - yj1516268@outlook.com

"""

import numpy as np


# int
arr_i = np.array([1, 2, 3, 4, 5, 6])
print(arr_i)
print(arr_i.dtype, "\n")


# Unicode
arr_u = np.array(list('hello'))
print(arr_u)
print(arr_u.dtype, "\n")


# bool
arr_b = np.array([True, False, False, True])
print(arr_b)
print(arr_b.dtype, "\n")


# object
class Like(object):
    pass


arr_o = np.array([Like(), Like()])
print(arr_o)
print(arr_o.dtype, "\n")
