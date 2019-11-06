from Q5input import *

# Your code - begin
output = []
if(len(l)>=n and n>0): #Not a valid input if n is negative
	for i in range(n,len(l)):
		output.append(l[i])
	for i in range(0,n):
		output.append(l[i])
else:
	output("Invalid Input")
# Your code - end
print output
