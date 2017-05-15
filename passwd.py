#!/usr/bin/env python
#_*_coding:utf-8_*_
#This is write by congpq

import getpass


_username = 'Stack Cong'
_password = 'qwe15716216'

username = input("username:")
password = getpass.getpass("password:")

#print(username,password)

if _username == username and _password == password:
	#print("Welcome user {name} login......".format(name=_username))
	print("   ")
	print("   ")
	print("    欢迎用户{name}登录......".format(name=_username))
else:
	#print("Invalid username or password!")
	print("非法！禁止登录本系统！")