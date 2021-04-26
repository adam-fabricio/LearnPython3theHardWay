"""Exercise 40 - Modules, Casses and Objects"""


class Song(object):

    def __init__(self, lyrics):
        if type(lyrics) is str:
            self.lyrics = lyrics.splitlines()
        else: 
            self.lyrics = lyrics

    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print()
    

    def count_line(self):
        print("This music have {} lines.".format(len(self.lyrics)))
        print()


    def count_chars(self):
        chars = 0
        for line in self.lyrics:
            chars += len(line)
        print(f"This music have {chars} chars.")
        print()

    
happy_bday = Song(["Hapy birthday to you",
                   "I don't get want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

happy_bday.sing_me_a_song()
happy_bday.count_line()
happy_bday.count_chars()

bulls_on_parade.sing_me_a_song()
bulls_on_parade.count_line()
bulls_on_parade.count_chars()

"""
Estudy drills.
1 - Write some more songs using this and make sure you
understand that you are passing a list of strings as 
the lyrics.
2 - Put the lyrics in a separate variable, then pass 
that variable to the class to use instead.
3 - see if you can hack on thi and make it do more 
things. Don't worry if you have no idea how, just 
give it a try and see what happens. 
Break it, thrash it, thrash it, you can hurt it.
"""

vossa_excelencia_letra = '''
Estão nas mangas
Dos Senhores Ministros
Nas capas
Dos Senhores Magistrados
Nas golas
Dos Senhores Deputados
Nos fundilhos
Dos Senhores Vereadores
Nas perucas
Dos Senhores Senadores

Senhores! Senhores! Senhores!
Minha Senhora!
Senhores! Senhores!
Filha da Puta! Bandido!
Corrupto! Ladrão! Senhores!
Filha da Puta! Bandido!
Senhores! Corrupto! Ladrão!

Sorrindo para a câmera
Sem saber que estamos vendo
Chorando que dá pena
Quando sabem que estão em cena
Sorrindo para as câmeras
Sem saber que são filmados
Um dia o sol ainda vai nascer
Quadrado!

Estão nas mangas
Dos Senhores Ministros
Nas capas
Dos Senhores Magistrados
Nas golas
Dos Senhores Deputados
Nos fundilhos
Dos Senhores Vereadores
Nas perucas
Dos Senhores Senadores

Senhores! Senhores! Senhores!
Minha Senhora!
Bandido! Corrupto
Senhores! Senhores!
Filha da Puta! Bandido!
Corrupto! Ladrão! Senhores!
Filha da Puta! Bandido!
Corrupto! Ladrão!

-"Isso não prova nada
Sob pressão da opinião pública
É que não haveremos
De tomar nenhuma decisão
Vamos esperar que tudo caia
No esquecimento
Aí então!
Faça-se a justiça!"

Sorrindo para a câmera
Sem saber que estamos vendo
Chorando que dá pena
Quando sabem que estão em cena
Sorrindo para as câmeras
Sem saber que são filmados
Um dia o sol ainda vai nascer
Quadrado!

-"Estamos preparando
Vossas acomodações
Excelência!"

Filha da Puta!
Bandido! Senhores!
Corrupto! Ladrão!
Filha da Puta!
Bandido! Corrupto! Ladrão!
Filha da Puta!
Bandido! Corrupto! Ladrão!
Filha da Puta!
Bandido! Corrupto! Ladrão!
'''

vossa_excelencia = Song(vossa_excelencia_letra)
vossa_excelencia.sing_me_a_song()
vossa_excelencia.count_line()
vossa_excelencia.count_chars()
