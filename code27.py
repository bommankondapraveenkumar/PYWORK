def BMI():
	A=input("enter I for inches and pounds, enter J for meters and kilograms")
	if A.lower()=="i":
		weight=float(input("enter weight in pounds"))
		height=float(input("enter height in inches"))
		
		BM=(weight/height**2)*703	
		print(f"{BM} BMI for given values")
	elif A.lower()=="j":
		weight=float(input("enter weight in kilograms"))
		height=float(input("enter height in meters"))
		
		BM=(weight/height**2)	
		print(f"{BM} BMI for given vlues")
	else:
		print("wrong input")
BMI()