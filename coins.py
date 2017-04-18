coin = 0
while True:
    print("You have {} coins".format(coin))
    want = input("Do you want a coin? ")
    if want == "yes":
        coin += 1
    elif want == "no":
        break

print("Bye")
