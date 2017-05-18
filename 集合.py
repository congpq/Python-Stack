#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

