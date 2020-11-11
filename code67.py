def ageprice():
	sum=0
	C=0
	K=0
	A=0
	G=0
	CH=0
	KI=0
	I=0
	AD=0
	line=input("enter the age of the family members each one age for a line:")
	while(line!=""):
		l=int(line)
		if(l<=2 and l>=0):
			C+=1;
			CH=C*0
			line=input("enter the age:")

		elif(l>2 and l<=12):
			K+=1;
			KI=K*14
			line=input("enter the age:")

		elif(l>=65):
			G+=1;
			I=G*18
			line=input("enter the age:")

		else:
			A+=1;
			AD=A*23
			line=input("enter the age:")

	print(f"cost for the zoo admission for family:${CH+KI+I+AD}")
ageprice()