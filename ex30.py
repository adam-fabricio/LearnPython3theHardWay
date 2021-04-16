"""Exercicio 30 - Else and if."""


people = 30
cars = 40
trucks = 15

# Compare if cars is grater than people
if cars > people:
    print("We should take the cars.")
# Compare if cars less than people
elif cars < people:
    print("We should not take the cars.")
# In other wise!
else:
    print("We can't decide.")

# Compare if trucks is greater than cars.
if trucks > cars:
    print("That's too many trucks.")
# Compare if trucks is less than cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Else
else:
    print("We still can't decide.")

# Compare if people is greater than trucks.
if people > trucks:
    print("Alright, let´s just take the trucks.")
# Else
else:
    print("Fine, let´s stay home then.")
