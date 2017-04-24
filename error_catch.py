#this is an error catcher.  make sure not to leave an empty area under
#the except line, or you could catch every single and slow down/crash system

while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops!  That was no valid number.  Try again...")
