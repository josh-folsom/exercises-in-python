pizza = input("Would you like some pizza?: ")
if pizza == "no":
    print("Have a salad")
if pizza == "yes":
    slices = int(input("How many slices can you eat?: "))
    if slices >= 1:
        print("call Papa Johns. ")
    else:
        print("Just have a salad.")
#else:
    #print("Have a salad.")
