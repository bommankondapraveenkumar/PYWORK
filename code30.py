def convert():
	P=float(input("Enter pressure in kilo pascals:\n"))
	F=P/6.895
	print(f"Pound-force per square inch: {F}")
	A=P/101
	print(f"Standard atmosphere: {A}")
convert()