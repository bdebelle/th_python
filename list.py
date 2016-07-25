#Run the script, to start using it.
#Put new things into the list one thing at a time.
#Enter the word done, in all caps, to quit the program.
#And once I quit, I want the app to show me everything that's on my list.
# only works with python3

shoppinglist = []

def my_list():
	task = input("Whatdaya Want? if nothing type 'DONE': " )
	if task != 'DONE':
		shoppinglist.append(task)
		my_list()
	else:
		print(shoppinglist)

my_list()

