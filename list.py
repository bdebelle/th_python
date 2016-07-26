#Run the script, to start using it.
#Put new things into the list one thing at a time.
#Enter the word done, in all caps, to quit the program.
#And once I quit, I want the app to show me everything that's on my list.
# only works with python3

# make a list that will hold onto our items
shopping_list = []
# Print instructions on how to use items
print("What would you like to remember?: ")
print("Type 'DONE' when finished")

def show_help():
  # Print instructions on how to use items
  print("What would you like to remember?: ")
  print("""
**************************
Enter 'DONE' when finished
Enter 'HELP' for this Help
Enter 'SHOW' to see your list
**************************
""")

show_help()  


def show_list():
    #Show list when user prompts
    print("Here is your list:" )
    print(shopping_list)

def add_to_list(new_item):
    #add new item to list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
    
while True:
    # Ask for new items
    new_item = input("> ")

    # Ask for new items to list
    
    # Be able to quit the app
    if new_item == 'DONE':
        break
    #Be able to offer Help
    elif new_item == 'HELP':
        show_help()
        continue
    #Show list on request
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)    
    
show_list()


