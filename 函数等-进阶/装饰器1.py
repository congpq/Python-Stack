#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
def timer(func):
    def deco(*args, **kwargs):
        star_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("The func run time is %s" %(stop_time-star_time))
    return deco

@timer  #test1=timer(test1)
def test1():
    time.sleep(1)
    print("Tihs is print test1!")

@timer  #test2=timer(test2)
def test2(name, age):
    print("test2:", name, age)


test1()
test2("Stack", 22)
