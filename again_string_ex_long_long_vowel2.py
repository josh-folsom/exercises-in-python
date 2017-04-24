#this one will not function
words = input("input some words with ee and oo in them: ")

for char in words:
    if char == 'oo':
        words = words.replace('oo', 'ooooo')
    elif char == 'ee':
        words = words.replace('ee', 'eeeee')
    else:
        pass
    print(words)
