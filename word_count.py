def word_count(x):
# defining file as a funtion

	file = open('word_count_file.txt','r')
	# opening and reading of the file

	y = file.read()
	# assigning value to the file

	a = len(y)
	b = len(y.split())
	c = len(y.split('\n'))
	d = len(set(y.split()))

	print(f'It contains\t{a} characters.\nIt contains {b} words.\nContains {c} lines.\nIt also contains {d} different or unique words.')
	# printing all result of assigned values in a sentence.

word_count('word_count_file.txt')
# to call the function