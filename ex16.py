"""Exercício 16 - Reaing and Writing Files."""


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the files. Godbye!")
target.truncate()

print("Now I'm going to ask and write tree lines.")
target.write("{}\n{}\n{}".format(input("line1: "),
             input("line2: "), input("line3: ")))

print("And finally, we close it.")
target.close()


"""Study Drills
1. Não aplicavel
2. Write a script similar to the last exercise that uses read and argv to read the file ou just created
3. There's too much repetitions in this file. Use strigs, formats, and escapes to print out line 1, line2 and line 3 with just one target.write() command insted of six)
4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you want to write a file
R. Because the default parameter is read not write.
5. If you ope the file with 'w' mod, then function and see if that's true.
R. Is truue, parameter w is alred truncated file.
"""


print('\n', 'x' * 20, ' Study drill - 2 ', 'x' * 20, sep='')

txt = open(filename)

print(f"Here´s is your file created: {filename}")
print(txt.read())

print("\n", 'x' * 20, " Study Drill - 3 ", "x" * 20, sep='')


