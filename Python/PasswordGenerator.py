import random
import string

def gen(LengthPassword):
    s = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)
    
    random.shuffle(s)
    
    password = "".join(s[0:LengthPassword])
    return password
    
LenPass = int(input("Enter the Length of Password:"))
    
print("Your Password is: \n" + gen(LenPass))
