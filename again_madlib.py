# this line asks the user to input a name and then capitalizes the input
name = input('What is your name?: ').capitalize()
# this line asks the user to input a subject and capitalizes the input
subject = input('What was your favorite subject in school?: ').capitalize()
# this prints a formatted string with both inputs assigned via curly brackets
print("{}'s favorite subject in school was {}.".format(name, subject))
