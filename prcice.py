#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "Stack Cong"
me = str.maketrans("Stack Cong","ABCDEFGHIJ")
print(name.translate(me))

print(name.ljust(40,"-"))
print(name.rjust(40,"+"))
print(name.isidentifier())