"""Exercise 38 - Doing Things to List."""


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Letś fix that.")

#  Divide a strings por espaços. split(ten_things)
stuff = ten_things.split(' ')
more_stuff = ['Day', "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

#  Conta o numero de itens na variavel e enquanto for menor de 
#  10, execute os próximos passos.
while len(stuff) !=10:
    #  Desempilhe o ultimo item da lista more_stuff e guarde na
    #  variavel next_one. pop(stuff)
    next_one = more_stuff.pop() # Erro (1) Digitado errado o next_one
    #  imprime o valor desempilhado
    print("Adding: ", next_one)
    #  adiciona por ultimo o item desempilhado. append(stuff(next_one))
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

#  Imprime o segundo item da lista
print(stuff[1])
#  Imprime o último item da pilha
print(stuff[-1])  # Whoa! fancy
#  Desempilhe o ultimo item e impirma.
print(stuff.pop())
# Junte os itens da lista com um ' ' entre cada item. join(' ', stuff)
print(' '.join(stuff)) # What? cool!
#  Junte o quarto e o quinto elemento da lista com # entre eles.
print('#'.join(stuff[3:5])) # Super stellar!

"""
1 - Take each function that is called, and go through the steps for 
functions calls to translate them to what Python does.
"""
