def parity():
	line=input("enter the parity: 8 bits:\n")
	while(line!=""):
		if(line.count==("0")+line.count==("1")!=8 or len(line)!=8):
			print("you dindt enter 8 bits enter 8 bits. ")
		else:
			ones=line.count("1")
		
			if(ones%2==0):
				print("the parity bit should be 0.")
			else:
				print("the parity bit should be 1.")
		line=input("enter 8 bits:" )
parity()