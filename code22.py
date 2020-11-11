import math
def atriangle():
	s1=float(input("enter the s1 side of a triangle: \n"))
	s2=float(input("enter the s2 side of a triangle: \n"))
	s3=float(input("enter the s3 side of a triangle: \n"))
	s=(s1+s2+s3/2)
	area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
	print(f"{area:.2f} is the area of the triangle for the given sides of the lenghts")
atriangle()
	