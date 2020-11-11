def season():
	M=input("enter the month name:\n")
	D=int(input("enter the date in the month:\n"))
		
	if(M.lower()=="march" and 20<=D<=31 or M.lower()=="april" and 1<=D<=30 or M.lower()=="may" and 1<=D<31 or M.lower()=="june" and 1<=D<=20):
		print(f"{M} {D} is in Spring day")
	elif(M.lower()=="june" and 21<=D<30 or M.lower()=="july" and 1<=D<=31 or M.lower()=="august" and 1<=D<=31 or M.lower()=="september" and 1<=D<=21):
		print(f"{M} {D} is in summer")
	elif(M.lower()=="september" and 22<=D<30 or M.lower()=="october" and 1<=D<=31 or M.lower()=="november" and 1<=D<=30 or M.lower()=="december" and 1<=D<=20):
		print(f"{M} {D} is in Fall")
	elif(M=="december"):
		if(D<21):
			print(f"{M}{D} is in Fall")
		else:
			print("is in Winter")
	else:
		print("is in Winter")
	
season()