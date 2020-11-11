def squarecolor():
	letter=input("enter the letter")	
	number=int(input("enter the number"))
	
	evencolum=['b','f','d','h']
	oddcolum=['a','c','e','g']
	evenrow=[2,4,6,8]
	oddrow=[1,3,5,7]
	
	if(letter in evencolum and number in evenrow or letter in oddcolum and number in oddrow):
		print("square is black")
	elif(letter in evencolum and number in oddrow or letter in oddcolum and number in evenrow):
		print("square is white")
	else:
		print("enter a letter first then a number")
squarecolor()