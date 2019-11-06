import math
print("Enter 2 smaller sides of right angled triangle");
a=input()
b=input()
if a>0 and b>0:
 a=a*a
 b=b*b
 hy = a+b
 print(math.sqrt(hy))
else:
 print("Invalid Input")

