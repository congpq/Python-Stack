#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("yesterday", 'r', encoding='utf-8')
# with open("yesterday", 'r', encoding='utf-8') as f:



f_new = open("yesterday2.bak", 'w', encoding='utf-8')

for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐等我去享受", "肆意的快乐等Alex去享受")
    f_new.write(line)
f.close()
f_new.close()
