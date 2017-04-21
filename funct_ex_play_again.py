def again():
    while True:
        again = input("Do you want to play again?: Y or N ")
        if again != "Y" and again != "N":
            print("incorrect reply, enter Y or N")
        else:
            if again == "Y":
                return True
            else:
                return False
                break

while True:
    again()
    if not again():
        break

print('Thanks for playing, goodbye!')

again()
