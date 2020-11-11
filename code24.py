def unitfotime():
	days=int(input("enter days:\n"))
	hours=int(input("enter hours:\n"))
	minutes=int(input("enter minutes:\n"))
	seconds=int(input("enter seconds:\n"))
	days=days*24*60*60
	hours=hours*60*60
	minutes=minutes*60
	seconds=seconds
	print(f"{days+hours+minutes+seconds} seconds of total")
unitfotime()