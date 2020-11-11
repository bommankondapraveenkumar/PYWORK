def leapyear():	
	Y=int(input("enter the year: "))
	
	A=Y%400
	B=A%100
	C=B%4

	if(A==0):
		print(f"{Y} is a leap year")
	elif(B==0):
		print(f"{Y} is a leap year")
	elif(C==0):
		print(f"{Y} is a leap year")
	else:
		print(f"{Y} is not a leap year")
		
leapyear()