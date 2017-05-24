#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
def test1():
    print("This is a scripts......")
    return 0

def test2():
    print("This is a scripts2......")


def test3():
    print("This is a scripts3......")
    return 1, 2, 3

x = test1(),
y = test2(),
z = test3()

print(x, y, z)

#默认参数特点：调用函数的时候，默认函数非必须传递
#默认参数用途：1.默认安装值  2.数据库安装值配置
def test(x,y=2):
    print(x)
    print(y)

  def conn(host,port=3306):
    pass

test(1),
conn('36.0.1.93')


#参数组 *args，实际参数数目不固定，形式参数设置为*args，此处args是参数名字，随便叫
def test8(*args):
    print(args)    #结果是元组 tuple

test8(1, 2, 3, 4, 5)
test8(*[1, 2, 3, 4, 5])   #列表变元组
'''

#**kwargs：把N个关键字参数转换成字典的方式
# def test9(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])   #字典读取方式
#     print(kwargs['age'])
#     print(kwargs['sex'])
#
# test9(name='Alex', age='9', sex='F')

# def test6(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# test6('Stack', age=8, sex='F')   #kwargs这个必须赋值键值对，否则错误

# def test4(name, age=8, **kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#
# test4('Stack', sex='F', hobby='tesla')

#args接受N个位置参数，转换成元组的方式
#kwargs接受关键字参数，转换成字典的方式
#位置参数不能写在关键字参数的后面
def test3(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test3('Satck', 199, sex='F', hobby='tesla')
