#!/usr/bin/env python
#教学视频第24集

product_list = [
    ('iPhone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120)
]
shopping_list = []


salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("您需要买那些物品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  #买的起商品
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩下[%s]啦，你还买个毛线啊！\033[0m" %salary)
            else:
                print("你想要购买的商品代码[%s]不存在！请重新输入商品编号！"%user_choice)
        elif user_choice == 'q':
            print("您已经购买的商品有：")
            for p in shopping_list:
                print(p)
            print("您的余额为：", salary)
            exit()
        else:
            print("Invalied Opeartion!")




        break