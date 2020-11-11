def timeformat():
	sec_perday=86400
	sec_perhour=3600
	sec_permin=60
	
	seconds=int(input("enter the seconds"))
	days=seconds/sec_perday
	seconds=seconds%sec_perday

	hours=seconds/sec_perhour
	seconds=seconds%sec_perhour
	
	minutes=seconds/sec_permin
	seconds=seconds%sec_permin
	
	print("the quivalent duration is ","%d:%02d:%02d:%02d"%(days,hours,minutes,seconds))
timeformat()
