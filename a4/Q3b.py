def diamond(n):

	# n should be odd
	if(n%2==1):

		# for first (n+1)/2 rows
		i=0
		while(i<(n+1)/2):
			# for space triangle
			j=i
			while(j<(n-1)/2):
				print("\b "),
				j+=1

			# for '*' triangle
			j=0
			while(j<2*i+1):
				print("\b*"),
				j+=1
			print
			i+=1

		# for last (n-1)/2 rows
		c=n-2
		i=0
		while(i<(n-1)/2):
			# for space triangle
			j=0
			while(j<(1+i)):
				print("\b "),
				j+=1
			# for '*' triangle
			j=c
			while(j>0):
				print("\b*"),
				j-=1
			print
			c-=2
			i+=1
