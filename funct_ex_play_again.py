play = ["Y"]

def again(play):
    play = input("Do you want to play again?: Y or N ")
    while play == "Y":
        return play

again(play)
