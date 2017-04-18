import random
my_random_number = random.randint(1, 10)
tries = 5
while True:
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What's the number? "))
    tries -= 1
    print("You have {} guesses to figure it out.".format(tries))
    if tries == 0:
        print("You ran out of guesses")
        break

    if guess == my_random_number:
        print("Yes! You win!")
        break
    elif guess < my_random_number:
        print("{} is too low".format(guess))

    elif guess > my_random_number:
        print("{} is too high".format(guess))
