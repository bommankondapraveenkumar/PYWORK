def Georgewillis():
	
	GeorgeWashington=1
	ThomasJefferson=2
	AbrahamLincoln=5
	AlexanderHamilton=10
	AndrewJackson=20
	UlyssesSGrant=50
	BenjaminFranklin=100

	D=int(input("Enter the denomination of currency:\n"))
	if(D==GeorgeWashington):
		print(f"${D} have GeorgeWashington")
	elif(D==2):
		print(f"${D} have ThomasJefferson")
	elif(D==5):
		print(f"${D} have AbrahamLincoln")
	elif(D==10):
		print(f"${D} have AndrewJackson")
	elif(D==20):
		print(f"${D} have UlyssesSGrant")
	elif(D==50):
		print(f"${D} have BenjaminFranklin")
	else:
		print("no such denomination exists")
Georgewillis()