try:
	f = open("car.py")
	for line in f:
		print(line, end="")
except IOError as message:
	print(message)
finally:
	f.close()
	print("file safely closed")