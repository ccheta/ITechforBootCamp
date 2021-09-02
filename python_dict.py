def students(**kwargs):
	print(kwargs)


name = input("What is your name?:")
age = int(input("How old are you?:"))
department = input("What department are you?:")

print(students(name=name,age=age,department=department))


