#!/usr/bin/env python
# -*- coding:utf-8 -*-

#递归
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("-->", n)

calc(10)

#高阶函数
def add(a, b, f):
    return f(a) + f(b)

res = add(3, -6, abs)
print(res)

def func1(arg1, arg2, *args, **kwargs):
    print(arg1),
    print(arg2),
    print(args),
    print(kwargs)

func1(1, 2, 4, 6, 99, name="alex", age=32)






