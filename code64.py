def pennies():
	sum=0.0
	total=0
	penniespn=5
	nickel=0.05
	P=input("enter the prices: ")
	while(P!=""):
		sum=sum+float(P)
		P=input("enter the prices: ")
	print(f"total payable amount is:{sum}")
	
	round=sum*100%penniespn
	if(round<penniespn/2):
		cash_total=round/100
	else:
		cash_total=total+nickel-round/100
	print(f"the amount is:{cash_total:.5f}")
pennies()