def cypher():

	message=input("enter the message:\n")
	shift=int(input("enter the number of shifts:\n"))
	
	
	for ch in message:

		if(ch>="a" and ch<="z"):
			pos=ord(ch)-ord("a")
			p=(pos+shift)%26
			new_char=chr(p+ord("a"))
			return new_char
		elif(ch>="A" and ch<="Z"):
			pos=ord(ch)-ord("A")
			p=(pos+shift)%26
			new_char=chr(p+ord("A"))
			return new_char
		else:
			ch

cypher()