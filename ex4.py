"""Exercicío 4 - Variaveis e nomes."""


# atribui valor a variável cars
cars = 100
# Atribui valor a variável space_in_cars
space_in_cars = 4.0
# Atribui valor a variável drivers
drivers = 30
# Atribui valor a variável average_passengers
passengers = 90
# Atribui valor a variável cars_not_driven a partir de outras variaveis
cars_not_driven = cars - drivers
# Atribui que a variavel drivers é a variavel drivers
cars_driven = drivers
# Atribui a variável carpool_capacity é carcars_driven vezes space_in_cars
carpool_capacity = cars_driven * space_in_cars
# atribui valor a variável
average_passengers_per_car = passengers / cars_driven

# Existem 100 carros disponiveis.
print("There are ", cars, "cars available.")
# Existem 30 motoristas disponiveis
print("There are only", drivers, "drivers avaliable.")
# Irá ter 70 carros vazios hoje.
print("There will be", cars_not_driven, "empty cars today.")
# Podemos transportar 120 pessoas hoje.
print("We can transport", carpool_capacity, "people today.")
# Temos 90 passageiros hoje.
print("We have", passengers, "to carpool today")
# Teremos que por 3 passageiros em cada carro.
print("We need to put about", average_passengers_per_car,
      "in each car.")
'''
1. Não é necessário especificar que space_in_cars é float
'''
# Testes do exercício
a = cars
print(a)
cars = 10
print(a)
