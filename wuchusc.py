def word_count(x):
	file = open('word_count_file.txt','r')

	y = file.read()

	print(len(y))
	# number of characters including white space
	print(len(y.split()))
	# number of words seperated by line spaces
	print(len(y.split('\n')))
	# number of lines in the file
	print(len(set(y.split())))
	# unique words(it is case sensitive)
	
	
word_count('word_count_file.txt')

	print(a)
	print(b)
	print(c)
	print(d)


	print("It contains" + ("a") + "characters and contains" + ("b") + "words in" + ("c") + "lines. It also contains" + ("d") + "different or unique words")