def decibel():	 
	D=float(input("Enter the decibel value sto know the sound name:\n"))

	if(D==40):
		print("It's Quiet Room")
	elif(D>=41 and D<70):
		print("Level between a Quiet Room and an Alarm Clock")
	elif(D==70):
		print("it's an Alarm Clock")
	elif(D>=71 and D<106):
		print("Level is betwee an Alarm Clock and GasLawnmower")
	elif(D==106):
		print("it's a Gas Lawnmower")
	elif(D>=107 and D<130):
		print("Level between a Gas Lawnmower and a Jackhammer")
	elif(D==130):
		print("It's Jackhammer ")
	elif(D>=131 and D<160):
		print("Level between a Jackhammer and an higher level sound making machine")
	else:
		print("error, value should be above 39 and below 161")
decibel()