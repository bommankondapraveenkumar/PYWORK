def CCD():
	mm=input()
	sm=int(input())
	if mm in ('c','C') and sm in (1,2,3):
		if sm==1:
			pr="COFFEE!"
		elif sm==2:
			pr="TEA"
		elif sm==3:
			pr="Maggie"
	elif mm in ('t','T') and sm in range(1,6):
		if sm==1:
			pr="Coc0cola!"
		elif sm==2:
			pr="sprite!"
		elif sm==3:
			pr="Thumbsup!"
		elif sm==4:
			pr="Maza!"
		elif sm==5:
			pr="SOFTDRINK!"
		elif sm==6:
			pr="coke!"
	else:
		print("INVALID CHOICE!")
		exit()
	print(f"Enjoy your {pr}.")
CCD()