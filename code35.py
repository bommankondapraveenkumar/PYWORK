def dogyear():
	ONE_HUM_YEAR=10.5
	AFTER_2=4
	H=float(input("enter the age of a dog"))	
	if(H>0 and H<=2):
		print(f"is equal to:{ONE_HUM_YEAR*H}  years equiuvalent to human age")
	elif(H>0 and H>2):
		print(f"{21+AFTER_2*(H-2)} years equiuvalent to human age")
	else:
		print("error")
dogyear()