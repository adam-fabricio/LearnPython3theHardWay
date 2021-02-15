"""Exercício 17 - More files."""


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {from_file} to {to_file}")

#  We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print("Ready, hit RETURN to continue. CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

"""Study Drills
1. The script is really annoying. There's no need to ask
you before doing the copy, and it prints too much out 
to the screen. Try to make the script  more friendly to 
use by removing features.

2. See now short you can make the script. I could make
this one line long.

3.
"""

print('\n', 'x' * 20, ' Study drill - 1 ', 'x' * 20, '\n', sep='')

print(f"Deseja copiar o arquivo {from_file} para {to_file}?")
print("Digite CTRL-C para cancelar, ou ENTER para continuar",
      end='')
input()

arquivoDeEntrada = open(from_file)
dadosDeEntrada = arquivoDeEntrada.read()

arquivoDeSaida = open(to_file, 'w')
arquivoDeSaida.write(dadosDeEntrada + "Study Drill 1")

arquivoDeEntrada.close()
arquivoDeSaida.close()

print(f"Copiado {len(dadosDeEntrada)} bytes.")

print('\n', 'x' * 20, ' Study drill - 2 ', 'x' * 20, '\n', sep='')

input(f"Será copiado o arquivo {from_file} para {to_file}.")

arquivoDeSaida = open(to_file, 'w')
arquivoDeSaida.write(open(from_file).read() + "Study Drill 2")
arquivoDeSaida.close()
