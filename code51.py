import math
def lettergrade():
	while True:
		G=input("enter the grade:")
		L=G[0]
		S=G[1]
		if(L=="A"):
			if(S=="+"):
				print("4.0")
			elif(S=="-"):
				print("3.7")
			else:
				print("4.0")
		elif(L=="B"):
			if(S=="+"):
				print("3.3")
			elif(S=="-"):
				print("2.7")
			else:
				print("3.0")
		elif(L=="C"):
			if(S=="+"):
				print("2.3")
			elif(S=="-"):
				print("1.7")
			else:
				print("2.0")
		elif(L=="D"):
			if(S=="+"):
				print("1.3")
			else:
				print("1.0")
		elif(L=="F"):
			print("0")
		else:
			print("invalid ")
lettergrade()