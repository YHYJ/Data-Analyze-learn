# -*- coding: utf-8 -*-

"""
Date: 2018-01-18 15:29:38
Last modified: 2018-01-18 15:29:38
Author: YJ1516 - yj1516268@outlook.com

"""

import numpy as np


"""rand()
生成指定维度大小为(3, 4)的随机二维浮点型数组，rand()的数据固定区间为0.0 ~ 1.0"""
arr_1 = np.random.rand(3, 4)
print(arr_1)
print(type(arr_1))

print("维度：{}维".format(arr_1.ndim))
print("维度大小：{}".format(arr_1.shape))
print("数据类型：{}\n".format(arr_1.dtype))


"""uniform()
生成指定维度大小为(3, 6, 2)的随机三维浮点型数组，指定数字区间为-1.0 ~ 5.0"""
arr_f = np.random.uniform(-1, 5, (3, 6, 2))
print(arr_f)
print(type(arr_f))

print("维度：{}维".format(arr_f.ndim))
print("维度大小：{}".format(arr_f.shape))
print("数据类型：{}\n".format(arr_f.dtype))


"""randint()
生成指定维度大小为(5, 2)的随机二维整型数组，指定数字区间为 3 ~ 6"""
arr_i = np.random.randint(3, 6, (5, 2))
print(arr_i)
print(type(arr_i))

print("维度：{}维".format(arr_i.ndim))
print("维度大小：{}".format(arr_i.shape))
print("数据类型：{}\n".format(arr_i.dtype))
