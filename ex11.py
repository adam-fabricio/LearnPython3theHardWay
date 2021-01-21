"""Exercício 10 - Asking Questions."""


print("How old are you?", end=' ')  # Imprime na tela, porem, ao final apenas da um espaço e não pula a linha
age = input()  # Le o teclado e guarda o valor na variavel
print("How tall are you?", end=' ')  # print igual ao aterior
height = input()  # Imput igual ao anterior
print("How much do you weight?", end=' ')  # Print igual ao anterior
weight = input()  # Input igual ao anterior

print(f"So, you're {age} old, {height} tall and {weight} heavy.")  # Print usando valor de variavies na foram de f""

print('\n', '*' * 60, '\n\n', sep='' , end='' ) # Print sem separador e sem pular linha

print('Então, você tem {} anos, {} de altura e {} de peso.'
     .format(age, height, weight))  # Print, inserindo as variaveis por meio de uma função inbuild da string str.format()

print('\n', '*' * 60, '\n\n', sep='', end='')  # Print para separar um print de outro

print('De novo, vc tem', age, 'anos,', height, 'de altura e', weight, 'de peso')  # Print inserindo o valor da variavel direto no meio do texto, ao meu ver a pior forma de fazer isso.


"""Study Drills

1. Go online and find out what Python's input does
2. Can you find other ways to use it? Try some of the samples you find
3. Write another "form" like this to ask some other questions
"""

