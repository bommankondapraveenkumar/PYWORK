def wavelen():
	W=int(input("Enter the Wavelength To know the Color: "))
	if(380<=W<450):
		print("Violet")
	elif(450<=W<495):
		print("Blue")
	elif(495<=W<570):
		print("Green")
	elif(570<=W<590):
		print("Yellow")
	elif(590<=W<620):
		print("Orange")
	elif(620<=W<=750):
		print("Red")
	elif(W<380):
		print("wavelength is below the range")
	elif(W>750):
		print("wavelength is above the range")
wavelen()