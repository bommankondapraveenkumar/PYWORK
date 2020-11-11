from math import *
def peripolygon():
	Q=float(input("enter the x coordinates:"))
	W=float(input("enter the y coordinates:"))
	
	perimeter=0
	prev_x=Q
	prev_y=W
	
	line=input("enter the x coordinates (blank space to exit):")
	
	while(line!=""):
		x=float(line)
		y=float(input("enter the y coordinates"))
		
		dist=sqrt((prev_x-x)**2+(prev_y-y)**2)
		perimeter=perimeter+dist
		
		prev_x=x
		prev_y=y
		
		line=input("enter the x coordinates (blank space to exit):")	
		
	dist=sqrt((Q-x)**2+(W-y)**2)
	perimeter=perimeter+dist
	print(f"perimeter for teh given polygon with x and y pair coordinates i s:{perimeter}")
peripolygon()