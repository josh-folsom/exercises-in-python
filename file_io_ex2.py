# Exercise 2 Write a program that prompts the user to enter a file name, then
# prompts the user to enter the contents of the file, and then saves the
# content to the file.

file_name = input("Enter name of file you would like to write: ")

def writer(file_name):
    file_handle = open(file_name, 'w')
    file_handle.write(file_name)
    file_handle.close()

    print(file_name)

writer(file_name)
