def loaves():
	sob=3.49
	dob=3.49*6/10
#enter the number of day old breads purchased by user#
	bread=float(input("enter the number of day old breads purchased"))
	real=sob*bread
	disc=dob*bread
	total=real-disc
	print("Actual price:     %5.2f"%real)
	print("discounted price: %5.2f"%disc)
	print("total discount:   %5.2f"%total)
loaves()