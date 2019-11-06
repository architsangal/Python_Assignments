def diamond():
	#	for printing first 3 rows
	i=0
	while(i<3):

		# for space triangle ==> a reverse loop
		j=i
		while(j<2):
			print("\b "),
			j+=1
		# for '*' triangle
		j=0
		while(j<2*i+1):
			print("\b*"),
			j+=1
		print
		i+=1

	#	for printing last 2 rows
	i=0
	while(i<2):

		# for space triangle
		j=0
		while(j<1+i):
			print("\b "),
			j+=1
		# for '*' triangle
		j=5
		while(j>4*i):
			print("\b*"),
			j += -2
		print
		i+=1
