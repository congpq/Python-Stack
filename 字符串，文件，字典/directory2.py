#!/usr/bin/env python
# -*- coding:utf-8 -*-

data = {
    '北京':{
        "东城区":{},
        "西城区":{},
        "朝阳区":{}
    },
    '山东':{
        "济南市":{},
        "威海市":{
            "文登区":{"米山镇","龙山路街道办事处"},
            "环翠区":{},
            "荣成市":{},
            "乳山市":{},
        },
        "青岛市":{}
    },
    '上海':{
        "普陀区":{},
        "闵行区":{},
        "闸北区":{}
    },
}

exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("请选择进入>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("请输入进入2>>:")
            if choice2 == "b":
                break
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("请输入进入3>>:")
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("最后一层，按b返回>>:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
