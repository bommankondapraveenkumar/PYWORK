def gradeavg():
	A=4.0
	A_plus=4.0
	A_mius=3.7
	B=3.0
	B_plus=3.3
	B_minus=2.7
	C=2.0
	C_plus=2.3
	C_minus=1.7
	D=1.0
	F=0.0
	invalid=-1
	sum=0
	count=0
	line=input("enter the grade:")
	while(line!=""):
		G=line
		L=G[0]
		S=G[1]
		if(L=="A"):
			if(S=="+"):
				sum=sum+A_plus;
				count=count+1;
			elif(S=="-"):
				sum=sum+A_minus
				count=count+1
			else:
				sum=sum+A
				count=count+1
			line=input("enter the grade:")
		elif(L=="B"):
			if(S=="+"):
				sum=sum+B_plus;
				count=count+1;
			elif(S=="-"):
				sum=sum+B_minus;
				count=count+1;
			else:
				sum=sum+B;
				count=count+1;
			line=input("enter the grade:")
		elif(L=="C"):
			if(S=="+"):
				sum=sum+C_plus
				count=count+1
			elif(S=="-"):
				sum=sum+C_minus
				count=count+1
			else:
				sum=sum+C
				count=count+1	
			line=input("enter the grade:")
		elif(L=="D"):
			if(S=="+"):
				sum=sum+D_plus
				count=count+1
			else:
				sum=sum+D
				count=count+1	
			line=input("enter the grade:")
	print(f"{sum/count}")
gradeavg()
		
	