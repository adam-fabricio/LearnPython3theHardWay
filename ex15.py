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

"""
