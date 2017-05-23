#!/usr/bin/env python
#_*_conding:utf8_*_

guess_of_age = 66

count = 0

#while True:
#	if count == 3:
#		break
while count<3:
#for i in range(3):
	age = int(input("The oldboy's age is:") )
	if age == guess_of_age:
		print("Yes,you got it!")
		break
	elif age > guess_of_age:
		print("Think smaller......")
	else:
		print("Think bigger! OK?")
		
	count = count +1
	
	if count == 3:
		continue_confirm = input("Dou you want to keep guessing?")
		if continue_confirm != 'n':
			count = 0

else:	
	print("You have tried too many times.Fuck off!")