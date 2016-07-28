import random

#generate a random number between 1 and 10

#secret_num = random.randint(1,10)

#guesses = []

def game():
	#compare guess to secret number
	secret_num = random.randint(1,10)
	guesses = []
	#Limit the number of guesses
	while len(guesses) < 5:
		try:
		#Catch When Someone submits a non-integer
		#get a number guess from the player
			guess = int(input("Pick a Number 1-10>" ))
		except ValueError:
			print("Only numbers moron. {} isnt a number".format(guess))
		else:
			if guess == secret_num:
		#print hit / miss
				print("You got it! my number was {}".format(secret_num))
				play_again()
			elif guess < secret_num:
				#Too Low Message
				print("my number is higher than {}".format(guess))
			else:
				#Too High Message
				print("my number is lower than {}".format(guess))
			guesses.append(guess)
	else:
		print("you didnt get it, my number was {}.".format(secret_num))

def play_again():
	#let people play again
	answer = input("Would you like to play again? Y/n? > ")
	if answer.lower() != 'n':
		game()
	else:
		print("bye")
		exit()

game()


