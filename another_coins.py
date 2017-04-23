coins = 0
print("You have {} coins".format(coins))
another = input("Do you want another?: ")

while another == "yes":
    coins = coins + 1
    print("You have {} coins".format(coins))
    another = input("Do you want another?: ")
    if another == "no":
        print("bye")
        break
