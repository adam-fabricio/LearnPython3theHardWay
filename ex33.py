"""Exercício 33 - While Loops."""

i = 0
numbers = []

while i < 6:
    print(f"At the top is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

''' Study drill - 1 -> Convert this while-loop to a function
that you can call, and replace 6 in the test (i < 6) with
a variable
3 - Add another variable to the function arguments that 
you can pass in that lets you change how much it 
increments by.
'''

def lista_de_numeros(tamanho, incremento):
    """Gera um lista de numero de números até o valor tamanho
    de incremento em incremento."""
    numbers = []
    i = 0
    

    while i < tamanho:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + incremento
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    return numbers

print("The numbers: ")

numbers = lista_de_numeros(10, 2)

for num in numbers:
    print(num)

