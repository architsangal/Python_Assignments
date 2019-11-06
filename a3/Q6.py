from Q6input import *

# Your code - begin

output=""

length=len(inp) # stores the length of the string

# making a dictionary with key as letter and value is frequency

dic={}

for i in range(length):
	ele=inp[i]
	if(not ele in dic):
	  	dic[ele]=1
	else:
		dic[ele]+=1

#list for storing type of frequency in "dic"
list=[]
for i in dic:
	if(not dic[i] in list):
		list.append(dic[i])

if(N<=len(list)):

	#making 2 different list one of dictionary and other of frequency

	alphabets=[]
	frequency=[]

	for i in dic:
		alphabets.append(i)
		frequency.append(dic[i])

	max=frequency[0]
	output=alphabets[0]
	index=0

	for i in range(N):

		for j in range(1,len(frequency)):

			if(frequency[j]>max):  #finding letter of max frequency and storing it in output

				max=frequency[j]
				output=alphabets[j]
				index=j

			elif(max==frequency[j]):# if frequency is same then store that letter which has lower ASCII value

				if(output>alphabets[j]):

					output=alphabets[j]
					index=j

		for j in range(len(frequency)):
	#making i th most occuring element's frequency zero so that for next iteration next most occuring element can be found out 

			if(max==frequency[j]):

				frequency[j]=0

		max=0

else: # if there are less than N type of frequency

	output="Invalid Input";

# Your code - end

print output
