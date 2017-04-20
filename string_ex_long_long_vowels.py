doubleVowel = ('oo', 'ooooo'), ('ee', 'eeeee'),
longString = "moose cheese ham house papoose tease meet."

new_longString = longString
for old, new in doubleVowel:
    new_longString = new_longString.replace(old, new)

print(new_longString)
