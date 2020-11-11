def monthname():
	E=input("enter the month name:\n")
	if(E=="january" or E=="march" or E=="may" or E=="july" or E=="august" or E=="october" or E=="December"): 
		print(f"31 days in {E} month")
	elif(E=="february"):
		print("if leap year 29 otherwise 28")
	elif(E=="april" or E=="june" or E=="september" or E=="november"):
		print(f"30 days in {E} month")
	else:
		print("check the spelling buddy, type name of months only")
monthname()