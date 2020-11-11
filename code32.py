def sorted():
	a=int(input("enter a value"))
	b=int(input("enter a value"))
	c=int(input("enter a value"))
	
	mn=min(a,b,c)
	mx=max(a,b,c)
	mid=a+b+c-mn-mx
		
	print(f"min:{mn}\n max:{mx}\n  mid:{mid}")
sorted()