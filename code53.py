def assesemp():

	rating=float(input("enter employee rating: "))
	if(rating==0.0):
		print(f"{2400*rating:.2f}\n is the raise and he has given an Unacceptable performance")
	elif(rating==0.4):
		print(f"{2400*rating:.2f} is the raise and he has given an Acceotable performance")
	elif(0.6<=rating<=1.0):
		print(f"{2400*rating:.2f} is the raise and he has given an Meritorious performance")
	else:
		print("invalid rating")
assesemp()