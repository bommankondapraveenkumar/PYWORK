def sumofdigits():
	D=int(input("enter digits: \n"))
	sum=0
	while(D>0):
		sum=sum+D%10
		print(sum)
		D=D//10
sumofdigits()