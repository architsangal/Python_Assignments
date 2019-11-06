from Q3input import *

# Your code - begin
letters={}
f=0 #flag variable

for i in inp:
	if((i>="a" and i<="z") or (i>="A" and i<="Z")): # checking if the letter is alphabet or not
#	if letter is not there in letters={}
#		then ==> add it
#		else ==> break the loop as the ans is False (here element gets repeated)
		i=i.lower()
		if(i in letters):
			f=1
			break
		else:
			letters[i]=1

if(f==0):
	output = "True"
else:
	output =  "False"


# Your code - end
print output
