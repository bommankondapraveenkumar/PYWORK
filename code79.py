import random
def max():
	count=0
	sound=0
	r=random.randint(0,100)
	while(r<=100 and count<=100):
		p=random.randint(0,100)
		if(r>p):
			print(f"{p}")
			count+=1
			p=random.randint(0,100)
		elif(r<p):
			print(f"{p} <===updated")
			r=p
			count+=1
			sound+=1
			p=random.randint(0,100)
	print(f"maximum value found was:{r}")
	print(f"maximum times updated:{sound}")
max()