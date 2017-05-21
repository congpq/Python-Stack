#!/usr/bin/env python
# -*- coding:utf-8 -*-

#data = open("yesterday", encoding="utf-8").read()
f = open("yesterday2", "r", encoding="utf-8") #定义一个文件句柄
print(f.tell())
#读到几个字符串
print(f.read(5))
#读几行
print(f.readline(3))
print(f.tell())

#返回最开始的地方
f.seek(0)

#打印文件的字符编码
print(f.encoding)
#返回操作系统内记录的内存中的编号
print(f.fileno())
#操作的文件或者字符是不是能够光标移动  布尔型
print(f.seekable())
#被操作文件是否可写
print(f.writable())
#强制刷新，将数据存入硬盘中
print(f.flush())
#文件需要设置为w的mode
#f.write("我爱北京天安门,\n")
#f.write("天安门上天上升\n")

#f.close()

