def Discount():
	count=0
	while(1):
		P=float(input("enter the prices:"))
		if(P==0):
			print("ivalid price")
			break;
		else:
			print(f" new price:{P*0.60:.2f} + discount:{P-P*0.60:.2f} + noriginal price:{P}")
		
Discount()