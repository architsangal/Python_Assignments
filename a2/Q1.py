from Q1input import *

# Your code - begin
length=len(inp)
output = ""
marks=[] # list for storing output in form of list 
c=0 #used for finding next character which is in turn used for comparing with next string
charcount=0 #count variable for counting character of same type and which are consecutive
for i in inp:
	c+=1
	charcount+=1
	if c==length : #for appending the last type of character and it's count
		marks.append(charcount)
		marks.append(i)
		break # otherwise index out of bound will occur as c=length
	if i!=inp[c] :
		marks.append(charcount)
		marks.append(i)
		charcount=0 # preparing charcount for counting next character
		
for i in marks :
	output=output+str(i)# transfering the correct output to variable output from marks
# Your code - end

print output
