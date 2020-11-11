def richterscale():
	magnitude=float(input("enter magnitude reading"))
	if(magnitude<1.9):
		print(f"{magnitude} is micro earthquake")
	elif(2<=magnitude<=2.9):
		print(f"{magnitude} is a very minor earthquake")
	elif(3<=magnitude<=3.9):
		print(f"{magnitude} is a minor earthquake")
	elif(4<=magnitude<=4.9):
		print(f"{magnitude} is a light earthquake")
	elif(5<=magnitude<=5.9):
		print(f"{magnitude} is a moderate earthquake")
	elif(6<=magnitude<=6.9):
		print(f"{magnitude} is a Strong earthquake")
	elif(7<=magnitude<=7.9):
		print(f"{magnitude} is a Major earthquake")
	elif(8<=magnitude<=9.9):
		print(f"{magnitude} is a Great earthquake")
	elif(magnitude>=10):
		print(f"{magnitude} is a Meteoric earthquake")
richterscale()