# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

# hcf by recursion
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b, a%b) # this is recursion as hcf() calls itself

# Reading numbers from user
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
