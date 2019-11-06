from Q5input import *

# Your code - begin
sets=[]
# to combine all possible strings of set1 and set2
for i in set1:

	for j in set2:

		sets.append(i+j)

output=0

for i in sets:

	i=i.lower()

	#converting all upper case character to lower case character so as to avoid complications of upper and lower case alphabets 		as "A" or "a" must be counted as same.

	alphabets={}

	for j in i:

		if(j>="a" and j<="z"): # checking that element is  alphabet

			if(not j in alphabets):# if that alphabet is not thereput it in alphabets

				alphabets[j]=1

	if(len(alphabets)==26):# if all alphabets are there then number of elements in variable "alphabets" == 26

		output+=1

	alphabets=[]# again making alphabets "empty" for processing new string 


print sets

# Your code - end

print output
