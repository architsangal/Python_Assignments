from Q7input import *

# Your code - begin
for i in l1:
	l2.append(i)
for i in range(0,len(l2)-1):
	for j in range(i+1,len(l2)):
		if(l2[i]>l2[j]):
			temp=l2[i]
			l2[i]=l2[j]
			l2[j]=temp

output=l2

# Your code - end
print output
