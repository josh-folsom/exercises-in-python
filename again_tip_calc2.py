bill = float(input("What was the bill amount?: $"))
service = input("What was the level of service? good / fair / bad : ")
people = int(input("How many people will split the bill?: "))

if service != "good" and service != "fair" and service != "bad":
    print("Incorrect input, try again")

if service == "good":
    totalbill = float(bill * 1.2)
    perperson = totalbill / people
    print("Total bill is ${}.  That's ${} per person".format(str(round(totalbill, 2)), str(round(perperson, 2))))

if service == "fair":
    totalbill = float(bill * 1.15)
    perperson = totalbill / people
    print("Total bill is ${}.  That's ${} per person".format(str(round(totalbill, 2)), str(round(perperson, 2))))

if service == "bad":
    totalbill = float(bill * 1.1)
    perperson = totalbill / people
    print("Total bill is ${}.  That's ${} per person".format(str(round(totalbill, 2)), str(round(perperson, 2))))
