import math
def lettergrade():
	while True:
		G=input("enter the grade:")
		L=int(G[0])
		D=G[1]
		S=int(G[2])
		print(f"{L}{D}{S}")
		if(L==4):
			if(S==0):
				print("A+")
		elif(L==3 and S==7):
			print("A")
		elif(L==3):
			if(S==3):
				print("B+")
			elif(S==0):
				print("B")
		elif(L==2 and S==7):
			print("B-")
		elif(L==2):
			if(S==3):
				print("C+")
			elif(S==0):
				print("C")
		elif(L==1 and S==7):
			print("C-")
		elif(L==1):
			if(S==3):
				print("D+")
			elif(S==0):
				print("D")
		elif(L==0):
			print("F")
	
		
		
		else:
			print("invalid ")
lettergrade()