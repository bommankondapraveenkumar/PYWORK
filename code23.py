import math
def polygon():
	n=float(input("enter the length of the sides"))
	s=float(input("enter the number of sides"))
	N=(n*s**2)
	D=math.tan(3.14/n)*4
	area=N/D
	print(f"{area} is the angle of lengths")
polygon()