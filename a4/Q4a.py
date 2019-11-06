def diamond():

	n=5	# we know that 5 is odd

#		dividing pattern in 6 parts(take " " as "_") ==>
#
#	    1)  _ _ _		2)	1	3)
#		_ _		       12		1	
#		_		      123		12
#
#	    4)  _		5)	12	6)	1
#		_ _			 1	
#

	#	for first (n+1)/2 rows
	i=0
	while(i<(n+1)/2):

#		for pattern 1)
		j=i
		while(j<=(n-1)/2):
			print " \b",
			j+=1

#		for pattern 2)
		j=1
		while(j<=i+1):
			print("\b"+str(j)),
			j+=1

#		for pattern 3)
		j=i
		while(j>=1):
			print("\b"+str(j)),
			j-=1
		print
		i+=1

	#	for last (n-1)/2 rows
	i=0
	while(i<(n-1)/2):

#		for pattern 4)
		j=0
		while(j<(1+i)):
			print("\b "),
			j+=1

#		for pattern 5)
		j=(n-1)/2-i-1
		c=0
		while(j>=0):
			c+=1
			print("\b"+str(c)),
			j-=1

#		for pattern 6)
		j=(n-1)/2-i-1
		while(j>0):
			c-=1
			print("\b"+str(c)),
			j-=1		
		print
		i+=1
