from Q3input import *

# Your code - begin
#multiplication is possible only when columns of first matrix is equal to rows of second matrix 
m=[[0 for mcol in range(len(m2[0]))]for mrow in range(len(m1))]
for i in range(0,len(m)):
	for j in range(0,len(m[i])):
		for k in range(0,len(m1[0])):
			m[i][j]=m[i][j]+m1[i][k]*m2[k][j];
output = m

# Your code - end
print output
