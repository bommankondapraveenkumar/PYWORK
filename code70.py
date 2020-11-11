def cypher():

	message=input("enter the message:\n")
	shift=int(input("enter the number of shifts:\n"))
	
	new_message=""
	for ch in message:

		if(ch>="a" and ch<="z"):
			pos=ord(ch)-ord("a")
			p=(pos+shift)%26
			new_char=chr(p+ord("a"))
			new_message=new_message+new_char
			
			print(new_message)
		elif(ch>="A" and ch<="Z"):
			pos=ord(ch)-ord("A")
			p=(pos+shift)%26
			new_char=chr(p+ord("A"))
			new_message=new_message+new_char
			
			print(new_message)
		else:
			new_message+ch

cypher()