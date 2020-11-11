sum=0	
count=0
while(1):
	n= int(input("enter the values"))
	if(n==0):
		print("end of input")
		break;
	sum+=n;
	count+=1;
if(count==0):
	print("no input given")	
else:
	avg=sum/count;
	print("average is :",avg)


