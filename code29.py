def convert():
	C=float(input("enter temperature in celcius to convert to F and K:\n"))
	if(not C<0):
		F=C+273.15	
		K=C*(9/5)+32
		print(f" Fahrenheit: {F}\n Kelvin:     {K}")
	else:
		print("Give positive values only")
convert()