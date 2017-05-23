#!/usr/bin/env python
# -*- coding:utf-8 -*-

#学习方法集  builtins.py

list_1 = [1,4,5,7,3,6,7,9]
#set是强制修改为集合的类型    int数据整型
list_1 = set(list_1)

list_2 = set( [1,4,5,8,7,9] )
print(list_1,list_2)

#取得交集
print( list_1.intersection(list_2) )
print( list_1 & list_2 )
#取得并集
print( list_1.union(list_2) )
print( list_1 | list_2)
#取得差集 集合前后有关系哟
print( list_1.difference(list_2) )
print( list_1 - list_2 )  #在list_1中，不在list_2中
print( list_2.difference(list_1) )
print( list_2 - list_1 ) #在list_2中，不在list_1中
#取得子集
print( list_1.issubset(list_2) )
#判断父集
print( list_1.issuperset(list_1) )
#判断对称差集  把两个互相之间没有的取出来，即是把交集去掉后的合集
print( list_1.symmetric_difference(list_2) )
print( list_1 ^ list_2 )
print('+++++++++++++++++++++++++++')
#两个集合有交集就返回False，无交集返回True
print( list_1.isdisjoint(list_2) )
print('----------------------')
list_1.add(999)
list_1.update([888, 555, 777])
print(list_1)
#remove如果值不存在set中将抛出异常
list_1.remove(555)
print(list_1)
#显示集合的长度
print( len(list_1) )
#888是否在集合list_1中  #列表、集合、字符串判断是否存在都是这么写
print( 888 in list_1)
print( 888 not in list_1)
#任意删除list_1中的某个元素并返回删除掉的这个元素
print( list_1.pop() )
#如果删除的元素不在集合中将不抛出异常
print( list_1.discard(0000))