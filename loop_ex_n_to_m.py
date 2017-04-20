start = input("What number should it start on?: ")
end = input("What number should it end on?: ")
count = int(start) - 1
for x in range(int(start), int(end), 1):
    while count < int(end):
        count += 1
        print(count)
