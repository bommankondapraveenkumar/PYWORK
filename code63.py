def conversion():
	while(1):
		T=float(input("enter the tempertaure in celcius"))
		for i in range(0,100):
			C=(T*9/5)+32
			print(f" CELCIUS:{T} TO FARHEINHEAT:{C}")
			T=T+10
			if(T>=100):
				break;
conversion()