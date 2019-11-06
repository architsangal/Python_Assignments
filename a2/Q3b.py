from Q3input import *

# Your code - begin
output = m1
trans=[[0 for tcol in range(len(m1))]for trow in range(len(m1[0]))]
for i in range(len(m1)):
	for j in range(len(m1[0])):
		trans[j][i]=m1[i][j]
output=trans
# Your code - end
print output
