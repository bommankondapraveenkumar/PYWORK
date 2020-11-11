def note():
	C4=261.63
	D4=293.66
	E4=329.63
	F4=349.23
	G4=392.00
	A4=440.00
	B4=493.88
	
	name=input("enter the name of the note: ")
	
	note=name[0]
	octave=int(name[1])
	
	if(note=="C"):
		freq=C4
	elif(note=="D"):
		freq=D4
	elif(note=="E"):
		freq=E4
	elif(note=="F4"):
		freq=F4
	elif(note=="G4"):
		freq=G4
	elif(note=="A4"):
		freq=A4
	elif(note=="B4"):
		freq=B4
	else:
		print("error")

	freq=freq/2**(4-octave)
	print(freq)
note()