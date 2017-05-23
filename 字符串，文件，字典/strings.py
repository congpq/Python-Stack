#!/usr/bin/env python

name = "alex"

print(name.capitalize())  #首字母大写
print(name.count("a"))    #name字符串中a记数几个
print(name.center(50,"#"))      #打印50个#符号，name的值放在中间显示
print(name.encode())
print(name.endswith("ex"))      #判断某字符串是以什么结尾
print(name.expandtabs())        #将tab键转换为多少个空格
print(name.find("x"))       #find中的字符在值中的编号，从0开始
print(name.format(name='alex',year=23))
print("=========",name.isalnum())    #阿拉伯数字+阿拉伯字符
print(name.isalpha())   #是否是纯英文字符
print(name.isdecimal())
print(name.isdigit())   #是否是一个整数
print(name.isidentifier())  #判断是不是一个合法的标识符(变量名)
print(name.islower())   #是不是都是小写
print(name.isnumeric()) #是不是一个整数
print(name.isspace())   #是不是一个空格
print(name.istitle())   #每个字符首字母都大写
print(name.isprintable()) #是否能够打印
print(name.isupper()) #字符串是不是全部都是大写
print(name.join(['1','2','3']))     #1alex2alex3   参数作为常量放在其中
print(name.ljust(50,'*'))   #保证打印的字符串长50，不够的用*补全
print(name.rjust(50,'-'))   #与上一个正好相反
print(name.lower())     #把大写变小写
print(name.upper())     #把小写变大写
print('Alex\n'.lstrip())    #去掉左边的空格或者回车
print('Alex\n'.rstrip())    #去掉右边的空格或者回车
print('\nAlex\n'.strip())   #左右回车与空格都去掉
print('-----------')
#加密可以简单使用此，前后两个字符串个数必须一致
p = str.maketrans("abcdef",'123456')
print("alex li".translate(p))
#=============
print('alex li'.replace('l','L',1)) #针对原字符串进行替换，第三位是替换其中的几个#结果是 aLex li
print('alex li'.rfind('l'))   #找到最右边的值的下标并返回
print('alex li'.split())    #以默认空格为分隔符，将原来的数据换乘数组 ['alex', 'li']
print('1+2\n+3+4'.splitlines())     #以换行为分隔符分成数组    ['1+2', '+3+4']
print('Alex Li'.swapcase())     #大写变小写，小写变大写
print('alex li'.title())    #把要操作的字符串变成title，每个字符串第一个字符大写
print('Alex Li'.zfill(50))   #字符长度不够要左边补位，默认是0补位  0000000000000000000000000000000000000000000Alex Li