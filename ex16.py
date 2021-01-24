"""Exercício 16 - Reaing and Writing Files."""


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the files. Godbye!")
target.truncate()

print("Now I'm going to ask you for tree lines.")
#  Original
#  line1 = input("line1: ")
#  line2 = input("line2: ")
#  line3 = input("line3: ")

#  Primeira tentaiva
#  all_lines = f"{line1}\n{line2}\n{line3}"

#  Segunda tentativa
all_lines = f"{input('line1: ')}\n{input('line2: ')}\n{input('line 3: ')}"


print("I'm goung towrite these to the file.")

target.write(all_lines)
#  target.write(line1)
#  target.write('\n')
#  target.write(line2)
#  target.write("\n")
#  target.write(line3)
#  target.write('\n')

print("And finally, we close it.")
target.close()


"""Study Drills
1. Não aplicavel
2. Write a script similar to the last exercise that uses read and argv to read the file ou just created
3. There's too much repetitions in this file. Use strigs, formats, and escapes to print out line 1, line2 and line 3 with just one target.write() command insted of six)
"""


print('\n', 'x' * 20, ' Study drill - 2 ', 'x' * 20, sep='')

txt = open(filename)

print(f"Here´s is your file created: {filename}")
print(txt.read())

print("\n", 'x' * 20, " Study Drill - 3 ", "x" * 20, sep='')


