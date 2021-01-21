"""Exercício 10 - Asking Questions."""


print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print('\n', '*' * 60, '\n', sep='')

print('Então, você tem {} anos, {} de altura e {} de peso.'
     .format(age, height, weight))

print('\n', '*' * 60, '\n', sep='')

print('De novo, vc tem', age, 'anos,', height, 'de altura e', weight, 'de peso')
