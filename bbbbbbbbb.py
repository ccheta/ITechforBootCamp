def word_count(x):
	# defining file as a funtion
	file = open('word_count_file.txt','r')
	# opening and reading of the file
	y = file.read()
	# assigning value to the file
	a = len(y)
	# assigning value to the lenght of characters including white space
	b = len(y.split())
	# assigning value to the lenght of words seperated by line spaces
	c = len(y.split('\n'))
	# assigning value to the lenght of lines in the file
	d = len(set(y.split()))
	# assigning value to the lenght of unique or different words(it is case sensitive)
	
	print(a)
	print(b)
	print(c)
	print(d)
	# printing result of assigned values individually.

	print("It contains\t"+str(a)+" characters,contains "+str(b)+" words in "+str(c)+" lines and also contains "+str(d) + " different or unique words.")
	# printing all result of assigned values in a sentence.
word_count('word_count_file.txt')
# to count words in the file