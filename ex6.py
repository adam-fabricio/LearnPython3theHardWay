"""Exercicio 6 - Strings e textos."""

# Define valor para variavel
types_of_people = 10
# Cria uma variavel x contendo uma string e inserindo outra variavel
# nessa string.
x = f"There are {types_of_people} types of people."

# Cria uma variavel contendo uma string
binary = "binary"
# Cria mais uma variável contendo uma string
do_not = "don't"

# Define a variável y contendo valor de duas outras variaveis
y = f"Those who know {binary} and those who {do_not}"  # 1 e 2

# imprime na tela o valor da variável x
print(x)
# Imprime na tela o valor da variável y
print(y)

# imprime na tela o valor da variavel x com uma string antes
print(f"I said: {x}")  # 3
# imprime na tela um texto contendo o valor de uma variável
print(f"I also said: '{y}'")  # 4

# Define um valor para variável hilarios
hilarios = False
# Define outro valor para a variável contendo um espaçõ para outra variável
joke_evaluation = "isn't that joke so funny?! {}"

# Imprime na tela o valor da variável adicionando um valor no lugar do {}
print(joke_evaluation.format(hilarios))

# Define o valor para w
w = "This is left side of ..."
# Define o valor para e
e = "a string with a right side."

# imprime na tela o valor de w + e
print(w + e)

"""Study Drills.
3 -  Sim, porque nos outros espaços eu estou inserindo um int na string e em
     outro momento estou inserindo um boolean.
4 - Porque ao somar as strings eu estou na verdade concatenando elas.
"""
