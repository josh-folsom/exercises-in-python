# Exercise 3
# Write a program that prompts the user to enter a file name, then prints
# the letter histogram and the word histogram of the contents of the file.
# notes:  I will attempt to build a function that takes the two functions from
# the word summary and the letter summary and combines them into one output.

# word summary function
def myHistogram(myList):
    myStatistic = {}
    for word in myList:
        if word not in myStatistic:
            myStatistic[word] = 1
        else:
            myStatistic[word] += 1
    print (word,myStatistic)

userinput = input("what file would you like to historgram? ").lower()
file = open(userinput,"r")
myHistogram(file.read().split())
file.close()
file = open(userinput,"r")
myHistogram(list(file.read()))
file.close()

#file = open(userinput,"r")
#lettercount={}
#for letter in list(file.read()):
    #if letter not in lettercount:
        #lettercount[letter] = 1
    #else:
        #lettercount[letter] += 1
#print (letter,lettercount)
#file.close();
#let_hist(list1)
