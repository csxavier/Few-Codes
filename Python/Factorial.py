# Generate Factorial of any no. 
# Factorial of n = n! = n * (n-1) * (n-2) * ... * 1
# E.g. -> Factorial of 5 = 5! = 5 * 4 * 3 * 2 * 1 = 120
# Keep Enter-ing values until you say "bye" (case-insensitive) 


def factorial(number):
    product = 1
    for i in range (1,number+1):
        product *= i
    return product

while (1):
    number = input("Enter a number (\"bye\" to exit) :")
    try:
        if (number.lower() != 'bye'):
            print ('{}! equals to {}'.format(number,factorial(int(number))))
        else:
            print ('{}! Have a nice Day.'.format(number.upper()))
            break
    except:
        print ('\"{}\" is not a valid Integer or Exit statement.'.format(number))

