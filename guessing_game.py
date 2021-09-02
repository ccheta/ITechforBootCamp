import random
# importing the random module
def guessing_game():
	# defining the title as a function
	number = random.randrange(0, 101)
	# stating range and running random values(last value not inclusive) 
	user_guess = int(input('Guess the right number: '))
	# setting the user's guessig platform,asking user input
	if user_guess > number:
		print('Higher')
	elif user_guess < number:
		print('lower')
	else:
		print('Winner')
		# printing result of strings assigned to conditions
guessing_game()
# calling of the function