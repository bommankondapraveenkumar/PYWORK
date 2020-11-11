def triangle():
	a=float(input("enter the a value"))
	b=float(input("enter the b value"))
	c=float(input("enter the c value"))
	if(a==b==c):
		print("its an equilateral triagle")
	elif(a==b and b is not c or b==c and a is not b or a==c and a is not b):
		print("its an isosceles")
	elif(a is not b is not c):
		print("its a scalene")
	else:
		print("error")
triangle()