# Exercise 3
# Write a program that prompts the user to enter a file name, then prints
# the letter histogram and the word histogram of the contents of the file.
# notes:  I will attempt to build a function that takes the two functions from
# the word summary and the letter summary and combines them into one output.

# word summary function


file=open("paragraph.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();

#letter summary function
dic = {'a': 0, 'b': 0, 'c': 0, 'd':0, 'e': 0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
dic2 = {}

word = input("Please type in a word: ").lower()
def let_hist(word):
    for i in word:
        dic[i] = dic[i]+1

    for key, value in dic.items():
        if value != 0:
            dic2[key] = value
    print(dic2)
let_hist(word)
