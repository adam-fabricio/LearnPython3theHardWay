"""Exercicio 3 - Mais variaveis e printing."""


name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Letś talk about {name}.")
print(f"He's {height} inchess tall.")
print(f"He's {weight} pounds havy.")
print("Actually that's not too havy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

""" Exercicios de estudo:
    1. Mude todas as variaveis tirando o my_
    2. contruir umas variavies que mudem inch para centimetros e pounds para
       kg. """


peso = weight * 0.453592
altura = height * 2.54

print(f"meu peso em kilos é {peso}.")
print(f"Minha altura em cm é {altura}")
