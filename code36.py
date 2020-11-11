def vowel():
	E=(input("enter the letter"))
	if(E=="a" or E=="e" or E=="i" or E=="o" or E=="u"):
		print(f"{E} is a vowel")
	elif(E=="y"):
		print(f"{E} is sometimes its a vowel and sometimes its a consonant")
	else:
		print(f"{E} is a consonant")
vowel()