from Q4input import *

# Your code - begin
# Using List Comprehension

list_of_zero=[x for x in inp if(x==0)] # x is used to (check the elements if they are equal to zero) and (store in list) 
list_without_zero=[x for x in inp if(x!=0)] # here x is used to (check the elements if they are not equal to zero) and (store in list)

output = list_without_zero+list_of_zero# adding the elements of the 2 list

# Your code - end
print output
