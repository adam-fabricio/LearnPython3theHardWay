"""Exercício 13 - Parameters, Unpacking, Variables."""


from sys import argv
#read the WYSS section for how to run this
print(argv)

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



"""Study Drills
1. Try giving fewer than three arguments to your scrept. See that error you get?
See if you can explain it.
R. Da erro de valor, o progrma estava esperando 4 paramentros mas obteve menos
2. Write a script that has fewer arguments and one that has more. Make sure you give the ynpacked variables good names.
R. Se colocar mais variaveis obetera erro, informando que espera 4 variaveis mas foi inserido mais argumentos


"""
