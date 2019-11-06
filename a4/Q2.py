def banner(m):
	length=len(m)	# length of message
	i=0

	#	for printing first row
	while(i<length+4):
		print ("\b*"),
		i += 1

	#	for printing second row
	print ("\n\b* "+m+" *")

	#	for printing last row
	i=0
	while(i<length+4):
		print "\b*",
		i+=1
