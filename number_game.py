import random

#generate a random number between 1 and 10

secret_num = random.randint(1,10)

while True:
	#get a number guess from the player
	guess = int(input("Pick a Number 1-10>" ))
	#compare guess to secret number
	if guess == secret_num:
		print("You got it! my number was {}".format(secret_num))
		break
	else:
		print("Wrong, try again")

#print hit / miss