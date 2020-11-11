def Lplate():
	P=input("enter the number plate:\n")
	if(len(P)==6 and P[0]>="A" and P[0]<="Z" and P[1]>="A" and P[1]<="Z" and P[2]>="A" and P[2]<="Z" and P[3]>="0" and P[3]<="9" and P[4]>="0" and P[4]<="9" and P[5]>="0" and P[5]<="9"):
		print("its an old license plate")
	elif(len(P)==7 and P[0]>="0" and P[0]<="9" and P[1]>="0" and P[1]<="9" and P[2]>="0" and P[2]<="9" and P[3]>="0" and P[3]<="9" and P[4]>="A" and P[4]<="Z" and P[5]>="A" and P[5]<="Z" and P[6]>="A" and P[6]<="z"):
		print("its a new license plate")
	else:
		print("its an invalid plate number: letters should be capital only!")
	
Lplate()