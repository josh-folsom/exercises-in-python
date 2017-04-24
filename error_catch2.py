#this is an error catcher.  make sure not to leave an empty field after
#the except: line, this one shows ValueError already.  you can do it but you
#could catch every single and slow down/crash system

while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
# this will replace the ValueError default message with an message of your own
# it can be done with any error message, particulary helpful with ones that are
# not descriptive.     
    raise ValueError("This is not a number.")
