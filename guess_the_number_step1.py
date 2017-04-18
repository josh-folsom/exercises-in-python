secret_number = 5
while True:
    print("I am thinking of a number between 1 and 10.")
    guess = float(input("What's the number? "))
    if guess == secret_number:
        print("Yes! You win!")
        break
    else:
        print("Nope, try again.")
