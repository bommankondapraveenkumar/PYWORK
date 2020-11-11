import math
def heat():
	c=4.186#heat capacity
	m=float(input("enter the mass"))#mass of matter in milliliters
	t=float(input("enter the temperature"))
	q=m*c*t
	print(f"{q:.2f} is total energy required")
	j=3600000
	K=q*2.777e-7
	r=K*8.9
	print(f"{r} cents costs to make coffee")
	
heat()
	
