try:
	f = open("car.py")
	for line in f:
		print line,
except IOError as message:
	print message
finally:
	f.close()
	print
	print "file safely closed"