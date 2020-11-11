import datetime
def nextday():
	Y=input("year-month-date")
	M=Y.split("-")
	print(M)
	Year=int(M[0])
	Month=int(M[1])
	date=int(M[2])
	dt=datetime.date(Year,Month,date)
	td=datetime.timedelta(days=-1)
	print(dt+td)
nextday()