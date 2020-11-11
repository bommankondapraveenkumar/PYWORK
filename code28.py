def WDI():
	Ta=float(input("enter the temperature in celcius:\n"))
	V=float(input("enter the wind speed in km/h format:\n"))
	if(Ta<=10 and V>4.8):
		WCI=13.12+0.6215*Ta-11.37*V**0.16+0.3965*Ta*V**0.16
		print(f'wind chill index: {WCI} ')
	else:
		print("Temperature should be less than or equal to 10C, Wind speed greater than 4.8 km/h")
WDI()