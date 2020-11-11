def palind():
	nam=input("enter:\n")
	em=("")
	while(nam!=""):
		for i in nam:
			em=i+em
		if(nam==em):
			print("yes")
			nam=input("enter:\n")
			
		else:
			print("no")
			nam=input("enter:\n")
palind()
