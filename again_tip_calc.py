bill = int(input("What was the bill amount?: $"))
service = input("What was the level of service? good / fair / bad : ")

if service != "good" and service != "fair" and service != "bad":
    print("Incorrect input, try again")

if service == "good":
    totalbill = float(bill * 1.2)
    print("Total bill is ${:.2f}".format(totalbill))

if service == "fair":
    totalbill = float(bill * 1.15)
    print("Total bill is ${:.2f}".format(totalbill))

if service == "bad":
    totalbill = float(bill * 1.1)
    print("Total bill is ${:.2f}".format(totalbill))
