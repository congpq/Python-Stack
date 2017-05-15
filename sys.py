#!/usr/bin/env python
#-*- encoding:utf -8-*-

'''
import sys

#print (sys.path) #打印环境变量

print(sys.argv)
print(sys.argv[2])
'''

import os

cmd_res = os.system("dir") #执行命令，不保存结果

cmd_res = os.popen("dir").read()  #把结果存在内存的一个位置，使用read命令读取结果
print("Local --> :",cmd_res)

cmd_res = os.mkdir("new_dir")   #在本地目录中新建一个目录，名字为：new_dir