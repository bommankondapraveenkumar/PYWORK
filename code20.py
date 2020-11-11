def idealgas():
	R=idealgasconst=8.314
	p=pressur=float(input("enter the pressure of the substance"))
	v=volume=float(input("enter the volume of the substance"))
	t=temperature=float(input("enter the  temperature of the substance"))
	kelvin = (t)
	n=p*v/(R/kelvin)
	print(f"{n:.2f} gas in moles")
idealgas()

##p = float(input("Enter the pressure in pascals:\n"))
#v = float(input("Enter the volume in liters:\n"))
#choice = input("Choose Fahrenheit, Celsius, or Kelvin (F / C / K):\n")
#if choice.lower() == "f":
  #temp = float(input("Enter the temperature:\n"))
 # kelvin = (temp - 32) * 5 / 9 + 273.15
#  n = p * v / 8.314 / kelvin
  #print("There are " + str(n) + " moles of gas.")
#elif choice.lower() == "c":
 # temp = float(input("Enter the temperature:\n"))
  #kelvin = temp + 273.15
  #n = p * v / 8.314 / kelvin
  #print("There are " + str(n) + " moles of gas.")
#elif choice.lower() == "k":
 # kelvin = float(input("Enter the temperature:\n"))
  #n = p * v / 8.314 / kelvin
  #print("There are " + str(n) + " moles of gas.")##

	
	