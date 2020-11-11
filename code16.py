import math
def varea():
	r=float(input("enter the radius\n"))	
	area=math.pi*r**2
	volume=4/3*math.pi*r**3
	print(f"{area:.2f} area\n")
	print(f"{volume:.2f} volume\n")
	if(r<=10 or r<=20):
		print("dont take values larger than 10 values")
	elif(r>20):
		print("good job")
varea()