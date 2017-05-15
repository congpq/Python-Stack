#!/usr/bin/env python
#_author_ = "Stack Cong"

#names = "ZhangYang Guyun Xiangpeng XuliangChen"

names = ["ZhangYang","Guyun",["Alex","jack"],"Xiangpeng","XuliangChen"]
print(names[0:-1:2])
print(names[::2])

#range(1,10,2)  #从第一个到最后一个数据，步长是2
#names2 = [1,2,3,4]
names2 = names.copy()
names2[2] = '丛培旗'
names.append("1111")
names[2][0] = "ALEX"
print("------------->",names)
'''
names.append("LeiHaidong")  #熟悉append方法
names.insert(1,"ChenRonghua")  #插入数据，参数中第一个参数是数据的位置，第二个参数是参数值
names.insert(3,"Xinzhiyu")
names[2] = "XieDi"
#删除目标数据
names.remove("ChenRonghua")
#del names[2] #删除信息
#names.pop()  #删除信息

#print(names)
#print(names[0],names[2])
#print(names[1:3]) #切片 #顾头不顾尾
#print(names[3])
#print(names[-1]) #-1是取属组中的最后一个值
#print(names[-3:-1]) #从左到右，值要依次减小
#print(names[-2:]) #位置是0的可以不写0，省略掉

#print(names.index("XieDi"))
#print( names[names.index("XieDi")] )
#print(names.count("XieDi"))
#names.clear()  #清空
names.reverse() #列表数据顺序反转
names.sort()  #数据排序
names.extend(names2)
del names2
#print(names,names2)
print(names)'''

import copy

person = ["a",100]

#浅copy
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
print(p1,p2,p3)