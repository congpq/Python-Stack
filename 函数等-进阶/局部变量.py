#!/usr/bin/env python
# -*- coding:utf-8 -*-

school = "Old boy"

def chang_name(name):
    global school   #声明全局变量
    school = "Mage Linux"
    print("Before change:", name, school)
    name = 'Stack Cong'
    age = 33
    print("After change:", name)

print("School:", school)
name = "Stack"
chang_name(name)
print(name)
