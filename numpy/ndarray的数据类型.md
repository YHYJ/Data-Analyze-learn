# ndarray的数据类型

> 通过ndarray的dtype来打印数组中元素的类型，ndarray常见的数据类型如下:

|      类型      | 类型代码  |            说明             |
| :----------: | :---: | :-----------------------: |
|  int8、uint8  | i1、u1 |   有符号和无符号的8位(1个字节长度)整型    |
| int16、uint16 | i2、u2 |   有符号和无符号的16位(2个字节长度)整型   |
| int32、uint32 | i4、u4 |   有符号和无符号的32位(4个字节长度)整型   |
|   float16    |  f2   |          半精度浮点数           |
|   float32    | f4或f  |         标准单精度浮点数          |
|   float64    | f8或d  |          双精度浮点数           |
|     bool     |   ?   |           布尔类型            |
|    object    |   O   |        Python对象类型         |
|   unicode    | <U1或U | 固定长度的unicode类型，跟字符串定义方式一样 |

#### 1. `dtype`参数

> 指定数组的数据类型，类型名+位数，如float64, int32

```python
# 创建一个ndarray，并将数据类型转为float64
float_arr = np.array([1, 2, 3, 4], dtype = np.float64)

print(float_arr)
# [ 1.  2.  3.  4.]

print(float_arr.dtype)
# float64

```

#### 2. `astype`方法

> 转换数组的数据类型

```python
# astype转换数据类型，将已有的数组的数据类型转换为int32
int_arr = float_arr.astype(np.int32)

print(int_arr)
# [1 2 3 4]

print(int_arr.dtype)
# int32
```