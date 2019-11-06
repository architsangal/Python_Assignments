def recurse(ans, n):
## Your code - begin
    if(n!=0):
    	ans=str(n%2)+ans
        return recurse(ans,n/2)
    elif(n==0 and ans!=""):# base condition
    	return int(ans)	# output is an integer
    else: # if above conditions is not satisfied that means that number which is to be converted from decimal to binary is 0
    	return 0
## Your code - end

def decToBin(n):
  return recurse("", n)

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output
