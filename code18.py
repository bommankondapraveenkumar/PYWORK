import math
def volcyl():
	radius=float(input("radius of a cylinder\n"))
	height=float(input("heught of a cylinder\n"))
	volume=math.pi*radius**2*height
	print(f"{volume:.2f} is the volume of a cylinder\n")
volcyl()