#!/usr/bin/env python
# -*- coding:utf-8 -*-

# decorator
# 装饰器就是个函数
# 目的是为了给其他函数添加附加功能
# 原则1：不能修改被装饰的源代码
# 原则2：不能修改被装饰的函数的调用方式

# 实现装饰器知识储备：
# 1.函数即变量
# 2.高阶函数
# 3.嵌套函数
# 高阶函数+嵌套函数=装饰器效果

import time

def test1():
    time.sleep(3)
    print('In the test1!')

test1()
