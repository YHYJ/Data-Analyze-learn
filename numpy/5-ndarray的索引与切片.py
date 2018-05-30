# -*- coding: utf-8 -*-

"""
Date: 2018-01-18 17:23:44
Last modified: 2018-01-18 17:23:44
Author: YJ1516 - yj1516268@outlook.com

"""

import numpy as np

# 一维数组的索引与切片
arr1 = np.arange(10)
print(arr1)
print(arr1[1:5], "\n")


# 多维数组的索引与切片
"""
arr[r1:r2, c1:c2]
arr[1, 1] 等价 arr[1][1]
[ : ] 代表某个维度的数据
"""
arr2 = np.arange(12).reshape(3, 4)
print(arr2)
print(arr2[1])      # 下标为1的行
print(arr2[1, 2])   # (1, 2)位置的数据
print(arr2[:, 1:3])  # 所有行中，列下标为1~3的数据，不包括3
print(arr2[0:2, 2:])    # (0~2, 2~)
print(arr2[:, 3])   # 所有行，列下标=3的

"""选取特定的子集时参数为列表"""
print(arr2[0:2, :])     # 行下标为0和2的数据
print(arr2[[0, -1], [1, 2]])  # 行下标为0，列下标为1 的数据；和行下标为-1，列下标为2的数据
print(arr2[[0, 1]][1:, 1:3], "\n")  # 先取行下标为0和1数据，再取结果中行下标为1~最后的列下标为1~3的数据


# 条件索引
"""条件索引返回一个一维数组"""
arr_year = np.array([[2010, 2011, 2012],
                    [2013, 2014, 2015],
                    [2016, 2017, 2018]])

is_year_after_2015 = arr_year >= 2015
print(is_year_after_2015, is_year_after_2015.dtype)
