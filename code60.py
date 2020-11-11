from random import *
def roulette():
	value=randrange(0,38)
	if(value==37):	
		print("Pay 00")
	else:
		print(f"The spin resulted in {value}")
	
	if(value==37):
		print("pay 00")
	else:
		print(f"pay {value}")
	
	if(value%2==1 and value>=1 and value<=9):
		print("Pay Red")
	if(value%2==0 and value>=12 and value<=18):
		print("Pay Red")
	if(value%2==1 and value>=19 and value<=27):
		print("Pay Red")
	if(value%2==0 and value>=30 and value<=36):
		print("Pay Red")
	elif(value==0 or value==37):
		pass
	else:
		print("Pay Black")

	if(value%2==0):
		print("pay even")
	else:
		print("pay odd")

	if(value>=1 and value<=18):
		print("pay 1 to 18")
	elif(value>=19 and value<=36):
		print("pay 19 to 36")
	else:
		print("pay 0 or pay 00")
roulette()