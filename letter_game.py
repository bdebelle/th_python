import os
import random
import sys
# make a list of words
words = [
	'apple',
	'apricot',
	'avocado',
	'banana',
	'bilberry',
	'blackberry',
	'blackcurrant',
	'blueberry',
	'boysenberry',
	'currant',
	'cherry',
	'cherimoya',
	'cloudberry',
	'coconut',
	'cranberry',
	'damson',
	'date',
	'dragonfruit',
	'durian',
	'elderberry',
	'feijoa',
	'fig',
	'gooseberry',
	'grape',
	'raisin',
	'grapefruit',
	'guava',
	'huckleberry',
	'jabuticaba',
	'jackfruit',
	'jambul',
	'jujube',
	'kiwifruit',
	'kumquat',
	'lemon',
	'lime',
	'loquat',
	'longan',
	'lychee',
	'mango',
	'marionberry',
	'melon',
	'cantaloupe',
	'honeydew',
	'watermelon',
	'mulberry',
	'nectarine',
	'nance',
	'olive',
	'orange',
	'clementine',
	'mandarine',
	'tangerine',
	'papaya',
	'passionfruit',
	'peach',
	'pear',
	'persimmon',
	'physalis',
	'plantain',
	'plum',
	'prune',
	'pineapple',
	'plumcot',
	'pomegranate',
	'pomelo',
	'quince',
	'raspberry',
	'salmonberry',
	'rambutan',
	'redcurrant',
	'salal berry',
	'salak',
	'satsuma',
	'strawberry',
	'tamarillo',
	'tamarind',
	'tomato',
	'yuzu'
	]

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
	clear()

	print('Strikes: {}/7'.format(len(bad_guesses)))
	print('')

	for letter in bad_guesses:
		print(letter, end=' ')
	print('\n\n')

	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_', end='')

	print('')


def get_guess(bad_guesses, good_guesses):
	while True:
		guess = input("Guess a letter: ").lower()

		if len(guess) != 1:
			print("You can only guess one letter!")
		elif guess in bad_guesses or guess in good_guesses:
			print("Youve already guessed that letter!")
		elif not guess.isalpha():
			print("You can only guess letters!")
		else:
			return guess

def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_guess(bad_guesses, good_guesses)

		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found = False
			if found:
				print("You Win!")
				print("The secret word was {}".format(secret_word))
				done = True
		else:
			bad_guesses.append(guess)
			if len(bad_guesses) == 7:
				draw(bad_guesses, good_guesses, secret_word)
				print("You Lost!")
				print("The Secret word was {}".format(secret_word))
				done = True
		if done:
			play_again = input("Play Again? Y/n ").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()

def welcome():
	start = input("Press enter/return to start or Q to quit").lower()
	if start =='q':
		print("Bye!")
		sys.ext()
	else:
		return True



print('Welcome to Letter Guess!')

done = False

while True:
	clear()
	welcome()
	play(done)
