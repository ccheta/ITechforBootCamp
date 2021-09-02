file = open('fetch_file.txt','r')
# opening and reading of file
x = {}

for line in file:
	listin = line.split(':')
	# assigning of values to target
	 
	if len(listin) < 2:
		continue
	x[listin[0]] = listin[1].strip()

print(x)
# printing result of strings assigned to condition



