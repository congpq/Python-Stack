#!/usr/bin/env python
# -*- coding:utf-8 -*-

#data = open("yesterday", encoding="utf-8").read()
#定义一个文件句柄
#读写模式
f = open("yesterday2", "r+", encoding="utf-8")
#写读模式，先新创建一个文件，再写进去内容  最常用的模式
f = open("yesterday2", "w+", encoding="utf-8")
#追加读写模式  在文件最后面增加
f = open("yesterday2", "a+", encoding="utf-8")
#二进制模式读操作的文件  二进制文件没有编码参数
f = open("yesterday2", "rb")
#二进制模式读操作的文件  二进制文件没有编码参数
f = open("yesterday2", "wb")
#string转换二进制byte类型
f.write("Hello word!\n".encode())
#第二个参数如果是w的话，就新建一个文件进行写入，r+既能读也能写
f = open("yesterday2", "a", encoding="utf-8")
print(f.tell())
#读到几个字符串
print(f.read(5))
#读几行 默认读一行
print(f.readline(3))
print(f.tell())

#返回最开始的地方
f.seek(0)
#查看句柄是否已经关闭
f.closed()

#字符串截断，从头开始阶段，参数可以是数字，字符数
f.truncate()
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
