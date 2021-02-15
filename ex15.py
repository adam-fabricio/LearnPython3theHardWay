"""Exercício 15 - Reading Files."""


#  From library 'sys' import the list of arguments 'argv'
from sys import argv
#  Unpackage the list 'argv' in two strings 'script' and 'filename'
script, filename = argv

#  Open a filen named by string in file name
txt = open(filename)

#  Print a text with a variable
print(f"Here´s your file {filename}:")
#  Print the content of file
print(txt.read())

#  Print new text
print("Type the filename again:")
#  Put a prompt '> ' and get value inputed
file_again = input("> ")

#  Open the file with the name typed
txt_again = open(file_again)

#  Print the content of file
print(txt_again.read())


"""Study Drills

1. Abouve each line, write out in English wat that line does.
2. If you are not sure, ask someone for help or search online. Many times searching for "python3.6 THING" will find answers to what that THING does in Python. Try searching for python3.6 open"
3. I used the word "commands" here but commands are also called "functions" and "methods." You will learn about functions and methods later int the book.
4. Get rid of the lines 10-15 where you used input and run the scriot again.
5. Use only input and try the script that way. Why is one way if getting the file name better than another?

6. Start python shell, and use open fro the pompt just like in thus origran. Notice  how you can open files and run read on them from whitin python3.6?
7. Have your scipt also call close() on the txt and txt_again variables. It's important to close files when you are done with them.

"""
