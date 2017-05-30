#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
user,passwd = 'alex','abc123'

def auth(func):
    def wrapper(*args, **kwargs):
        username = input("Please input your username:").strip()
        password = input("Please input your password:").strip()
        if user == username and passwd == password:
            print("\033[32;1mUser has passed Authentication!\033[0m")
            func(*args, **kwargs)
        else:
            exit("\033[32;1mInvalued username or password!\033[0m")
    return wrapper

def index():
    print("Welcom to index page!")
@auth
def home():
    print("This is your HOME!!")
@auth
def bbs():
    print("This is a BBS!!!")

index()
home()
bbs()
