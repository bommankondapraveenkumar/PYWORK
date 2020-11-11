import string
l=input("enter a string:\n")
li=l.replace(" ","")	
line=li.translate(str.maketrans('', '', string.punctuation))
	
is_palindrome=True

for i in range(0,len(line)//2):
	if(line[i]!=line[len(line)-i-1]):
		is_palindrome=False
if(is_palindrome):
	print(line,"is a palindrome")
else:
	print(line,"is not a palindrome")