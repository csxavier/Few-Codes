# Convert Temp from Kelvin, Celsius and Fahrenheit  
# to any of the Kelvin, Celsius and Fahrenheit
# Enter Below Params:
#		Temp: 
#		fromScale : K or C or F (case in-sensitive)
#		toScale : K or C or F (case in-sensitive)
#

def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0

def ktoc(temp):
    return temp - 273.15

def ctok(temp):
    return temp + 273.15

def convert(temp, fromScale, toScale):
    if fromScale == "c" or fromScale == "C":
        if toScale == "f" or toScale == "F":
            return ctof(temp)
        elif toScale == "k" or toScale == "K":
            return ctok(temp)
        else:
            print ("wrong scale input")
    elif fromScale == "f" or fromScale == "F":
        if toScale == "c" or toScale == "C":
            return ftoc(temp)
        elif toScale == "k" or toScale == "K":
            return ctok(ftoc(temp))
        else:
            print ("wrong scale input")
    elif fromScale == "k" or fromScale == "K":
        if toScale == "c" or toScale == "C":
            return ktoc(temp)
        elif toScale == "f" or toScale == "F":
            return ctof(ktoc(temp))
        else:
            print ("wrong scale input")
    else:
        print ("wrong scale input")

temp = int(input("Enter a temperature :"))
fromScale = input("Enter the scale to convert from :")
toScale = input("Enter the scale to convert to :")

convertedtemp = convert(temp, fromScale, toScale)

print("The Temp: {}{} is {}{}".format(temp, fromScale , convertedtemp, toScale))
