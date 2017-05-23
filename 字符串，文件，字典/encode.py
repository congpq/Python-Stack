#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "你好"
print(s, type(s))
s_to_gbk = s.encode('gbk')

print(s_to_gbk)


gbk_to_utf8 = s_to_gbk.decode('gbk').encode('utf-8')
print(gbk_to_utf8)

