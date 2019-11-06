from Q1input import *

# Your code - begin
length=len(inp)        # variable "length" is length of "inp" list
list=inp
dic={}                 #"dic" is a dictionary which will have the desired output

for i in range(len(list)): # extracting  index of elements of list one by one
  ele=list[i]          #storing element in variable "ele" for convenience
  if(not ele in dic):  # checking if the element is not there
  	dic[ele]=1     #if element is not there add  it in  dictionary
  else:
	dic[ele]+=1    #if element is there increase the value of key.

output = dic           # This is the answer for the given input.
# Your code - end

print output
