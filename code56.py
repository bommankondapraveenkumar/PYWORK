from math import *
def phonebill():
	planm=50	
	plant=50
	at=0.15
	am=0.25
	sc=0.44
	
	minutes=int(input("enter the number of minutes used: "))
	texts=int(input("enter the number of texts used: "))	
	if(minutes<=50 and texts<=50):
		TOT=(15+15+0.44)
		TOTAL=TOT+TOT*0.05
		print(f"Bill: {TOTAL:.2f}")
	elif(minutes>50):
		if(texts>50):
			em=minutes-50
			et=texts-50
			TOT=(15+(em)*0.25+15+(et)*0.15+0.44)
			TOTAL=TOT+TOT*0.05
			print(f"Bill: {TOTAL:.2f}\n EXTRA MIN:{em}\n EXTRA TEX:{et}")
		elif(texts<50):
			em=minutes-50
			TOT=(15+(em)*0.25+15+0.44)
			TOTAL=TOT+TOT*0.05
			print(f"Bill: {TOTAL:.2f}\n EXTRA MIN:{em}")
		else:
			print("Invalid entry")	
	elif(minutes<50):
		if(texts>50):
			et=texts-50
			TOT=(15+15+(et)*0.15+0.44)
			TOTAL=TOT+(TOT*0.05)
			print(f"Bill: {TOTAL:.2f}\n EXTRA TEX:{et}")
		elif(texts<50):
			em=minutes-50
			TOT=(15+15+0.44)
			TOTAL=TOT+TOT*0.05
			print(f"Bill: {TOTAL:.2f}\n EXTRA MIN:{em}")
		else:
			print("Invalid entry")
	
phonebill()