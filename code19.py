import math
def deter():
	d=float(input("enter the height of object is thrown in meters(m)"))
	a=gravity=9.8
	vi=0
	vf=math.sqrt(vi**2+2*a*d)
	print(f"{vf:.2f} m/s^2 is the final velocity of the object")
deter()
	