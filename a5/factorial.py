def factorial(n):
## Your code - begin
	if(n<0):
		return -1  #error message
	if(n==0):  #base condition
		return 1
	else:
		return n*factorial(n-1)  #recursion
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = factorial(n)
	print output
