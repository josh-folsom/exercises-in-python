import random
my_random_number = random.randint(1, 10)
while True:
    print("I am thinking of a number between 1 and 10.")
    guess = float(input("What's the number? "))
    if guess == my_random_number:
        print("Yes! You win!")
        break
    elif guess < my_random_number:
        print("{} is too low".format(guess))
    elif guess > my_random_number:
        print("{} is too high".format(guess))
