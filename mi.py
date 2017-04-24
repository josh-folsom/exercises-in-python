alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
text = "lbh zhfg hayrnea jung lbh unir yrnearq"
newtext = ""
for letter in text:
    if(letter == " "):
        newtext += " "
    else:
        index = alphabet.index(letter)
        newIndex = (index + 13 + 26) % 26
        newtext += alphabet[newIndex]
print(newtext)
