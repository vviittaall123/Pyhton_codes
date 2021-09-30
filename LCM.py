# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
      greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


# lcm by recursion
def lcm(a,b):
    lcm.multiple=lcm.multiple+b
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple=0
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    LCM=lcm(b,a)
else:
    LCM=lcm(a,b)
print(LCM)
