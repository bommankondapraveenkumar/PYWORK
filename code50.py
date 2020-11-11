import math
import cmath
def quadretic():	
	a=float(input("enter the a value"))
	b=float(input("enter the b value"))
	c=float(input("enter the c value"))
	disc=b**2-4*a*c
	print(disc)
	if(disc==0):
		sol1=(-b+cmath.sqrt(disc))/2*a
		print(f"{sol1} the equation has one real root")
	elif(disc>0):
		sol1=(-b+cmath.sqrt(disc))/2*a
		sol2=(-b-cmath.sqrt(disc))/2*a
		print(f"{sol1:.2f} and {sol2:.2f} are two roots for the given equation")
	elif(disc<0):
		print("zero roots")
quadretic()