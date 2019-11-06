def recurse(n, i):
## Your code - begin
	if(i==0):# considering Abcba is also palindrome
		n=n.lower()
	if(i<=len(n)/2):#REVERSING STRING ==> first half of the elements of string is exchanged with last half of string
# e.g.    abc replace "a" with "c" to reverse the string as cba
# e.g.    abcd replace "a" with "d" and replace "b" with "c" to reverse the string as dcba
		if(i!=0):
# swaping two elements keeping all other elements same.
			n=n[0:i-1]+n[len(n)-i]+n[i:len(n)-i]+n[i-1]+n[len(n)-i+1:]
			return recurse(n,i+1)
		else:
			rev=recurse(n,1)  # as this recursion is executed first hence it is at bottom of stack so final reversed string come back here which is stored in "rev"
			if(rev==n):#  condition of palindrome
				return True
			else:
				return False
	return n
## Your code - end

def isPalindrome(n):
  return recurse(n, 0)

if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output
