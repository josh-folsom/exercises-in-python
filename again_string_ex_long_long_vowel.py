doubleVowel = ('oo', 'ooooo'), ('ee', 'eeeee'),
words = input("input some words with ee and oo in them: ")

for old, new in doubleVowel:
    words = words.replace(old, new)

print(words)
