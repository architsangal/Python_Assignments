from Q6input import *

# Your code - begin
for i in range(0,len(l)-1):# for different passes... last pass is not required so it is len(l)-1
	for j in range(i+1,len(l)):# loop from next element till end
		if(l[i]>l[j]):
			temp=l[i]
			l[i]=l[j]
			l[j]=temp
median=0
if(len(l)%2==1):
	median=l[(len(l)-1)/2]
else:
	median=(l[(len(l)-2)/2]+float(l[len(l)/2]))/2;
output=median


# Your code - end
print output
