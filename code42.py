def freqtonotes():
	
	C4=261.63
	D4=293.66
	E4=329.63
	F4=349.23
	G4=392.00
	A4=440.00
	B4=493.88
	limit=1

	NF=float(input("enter the frequency:\n"))
	if(NF==C4 or C4-limit<=NF<=C4+limit):
		print(f"{NF}is  a C4 note")
	elif(NF==D4 or D4-limit<=NF<=D4+limit):
		print(f"{NF}is  a D4 note")
	elif(NF==E4 or E4-limit<=NF<=E4+limit):
		print(f"{NF}is  a E4 note")
	elif(NF==F4 or F4-limit<=NF<=F4+limit):
		print(f"{NF}is  a F4 note")
	elif(NF==G4 or G4-limit<=NF<=G4+limit):
		print(f"{NF}is  a G4 note")
	elif(NF==A4 or A4-limit<=NF<=A4+limit):
		print(f"{NF}is  a A4 note")
	elif(NF==B4 or B4-limit<=NF<=B4+limit):
		print(f"{NF}is  a B4 note")
	else:
		print("error, only within rangin 1 HZ it will consider from actual notes")

freqtonotes()