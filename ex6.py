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
y = f"Those who know {binary} and those who {do_not}"

# imprime na tela o valor da variável x
print(x)
# Imprime na tela o valor da variável y
print(y)

# imprime na tela o valor da variavel x com uma string antes
print(f"I said: {x}")
# imprime na tela um texto contendo o valor de uma variável
print(f"I also said: '{y}'")

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

"""Study Drills."""
