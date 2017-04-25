# Write a word_histogram function that takes a paragraph of text as its input,
# and returns a dictionary containing the tally of how many times each word in
# the alphabet was used in the text. For example:

#>>> word_histogram('To be or not to be')
#{'to': 2, 'be': 2, 'or': 1, 'not': 1}

file=open("paragraph.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();
