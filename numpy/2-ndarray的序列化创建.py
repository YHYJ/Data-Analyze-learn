# -*- coding: utf-8 -*-

"""
Date: 2018-01-18 15:58:56
Last modified: 2018-01-18 15:58:56
Author: YJ1516 - yj1516268@outlook.com

"""

import numpy as np


# np.array(list, dtype)
"""list为序列性对象或嵌套序列性对象，dtype表示数据类型"""
arr = np.array(range(1, 10))
print(arr)
print(type(arr))
print("维度：{}维".format(arr.ndim))
print("维度大小{}\n".format(arr.shape))

list_of_list = [range(10), range(10)]
arr_lol = np.array(list_of_list)
print(arr_lol)
print(type(arr_lol))
print("维度：{}维".format(arr_lol.ndim))
print("维度大小{}\n".format(arr_lol.shape))


# np.zeros()
"""指定大小的全0数组
注意：第一个参数是元组，用来指定维度大小，如(3, 4)
      第二个参数可以指定类型，如int，默认为float"""
arr_zeros = np.zeros((3, 4))
print(arr_zeros)
print(type(arr_zeros))
print("维度：{}维".format(arr_zeros.ndim))
print("维度大小{}\n".format(arr_zeros.shape))


# np.ones()
"""指定大小的全1数组
注意：第一个参数是元组，用来指定大小，如(3, 4)
      第二个参数可以指定类型，如int，默认为float"""
arr_ones = np.ones((3, 4))
print(arr_ones)
print(type(arr_ones))
print("维度：{}维".format(arr_ones.ndim))
print("维度大小{}\n".format(arr_ones.shape))


# np.arange()
"""arange() 类似 python 的 range()，用来创建一个一维 ndarray 数组
结果等同于 np.array(range())"""
arr_arange = np.arange(1, 12, 2)    # 范围 步长
print(arr_arange)
print(type(arr_arange))
print("维度：{}维".format(arr_arange.ndim))
print("维度大小{}\n".format(arr_arange.shape))


# np.reshape()
"""重新调整数组的维度"""
arr_arange = np.arange(1, 13)
print(arr_arange, "\n")
arr_reshape = arr_arange.reshape(3, 4)  # 3x4个元素，二维数组
print(arr_reshape, "\n")
arr_reshape = arr_arange.reshape(2, 2, 3)  # 2x2x3个元素，三维数组
print(arr_reshape, "\n")


# np.random.shuffle()
"""打乱数组序列，随机重新排列"""
arr_arange = np.arange(1, 13)
print(arr_arange, "\n")
np.random.shuffle(arr_arange)
print(arr_arange, "\n")
