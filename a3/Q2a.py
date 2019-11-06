from Q2input import *

# Your code - begin
final_Dic={}# final dictionary to store addition of elements of Dic1 and Dic2

for i in Dic1:
	if(i in Dic2):
		final_Dic[i]=Dic1[i]+Dic2[i]    # adding values of common keys
	else:
		final_Dic[i]=Dic1[i]		# putting non common element of Dic1 in final_Dic

for i in Dic2:
	if(not i in Dic1):	
		final_Dic[i]=Dic2[i]		# putting non common element of Dic2 in final_Dic

output = final_Dic 
# Your code - end
print output
