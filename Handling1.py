print('fff')
try:
	num = int(input('how old are you: '))
	print(num + 5)
except SyntaxError as e:
	print("you can only pass in numbers.Try again!")
except:
	print("you have made a mistake!")
else:
	print('you are good to go!')

	import random

def guessing game():
	number = random.randrange(0,101)
	user_guess = int(input("guess the number:"))

	if user_guess > number:
		print("too high")
	elif user_guess < number:
		print("too low")
	else user_guess = number:
		print("just right")

		"guessing game" ()
	pass