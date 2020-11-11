from math import *
def fretoname():
	P=input("enter the Frequency to get name: ")
	W=eval(P)
	if(W<3*10**9):
		print("Radio Waves")
	elif(3*10**9<=W<3*10**12):
		print("Microwaves")
	elif(3*10**12<=W<4.3*10**14):
		print("Infrared Light")
	elif(4.3*10**14<=W<7.5*10**14):
		print("Visible Light")
	elif(7.5*10**12<=W<3*10**17):
		print("Ultraviolet Light")
	elif(3*10**17<=W<3*10**19):
		print("X-Rays")
	elif(W>=3*10**19):
		print("Famma rays")
	else:
		print("Invalid Entry")	
fretoname()