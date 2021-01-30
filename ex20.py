"""Exercício 20 - Functions and Files."""

#  Import argv list from library sys
from sys import argv

#  Unpack argv list
script, input_file = argv

#  Defines the print_all function that receives a parameter
def print_all(f):
    #  Print the value of object f.
    print(f.read())

#  Defines the rewind funcition that receives a parameter
def rewind(f):
    #  Return to initial line
    f.seek(0)

#  Defines the print_a_line function. This function print one line
def print_a_line(line_count,f):
    #  Print number of line and the line
    print (line_count, f.readline())

#  Get the object of the file
current_file = open(input_file)

#  Print one line on screen
print("First let's print the whole file: \n")

#  Print all file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#  Return to initial line
rewind(current_file)

print("Let's print three lines:")

#  Defines the corruent line value
current_line = 1
#  Print First line
print_a_line(current_line, current_file)

#  Add one to the current_line variable
current_line = current_line + 1

#  Print second line
print_a_line(current_line, current_file)

#  Add one to the current_line variable
current_line = current_line + 1
#  Print third line
print_a_line(current_line, current_file)

"""Study Drill
1. Write English comments for each line to inderstand what that line does.
"""
