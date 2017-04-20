leetspeak = ('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7')
longString = """Four score and seven years ago our fathers brought forth on
this continent, a new nation, conceived in Liberty, and dedicated to the
proposition that all men are created equal. """.upper()

new_longString = longString
for old, new in leetspeak:
    new_longString = new_longString.replace(old, new)

print(new_longString)
