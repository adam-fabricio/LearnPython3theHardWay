"""Exercício 35 - Design and Debug."""


from sys import exit

# Função de derrota no jogo
def derrota(pq):
    print(pq, "BOM JOGO!")
    exit()

# Função de vitória
def vitoria(mensagem):
    print(mensagem, "PARABENS, VOCE SE TORNOU UM TREINADOR POKEMON")
    exit()


# Inicio do jogo
def start():
    print("BEM VINDO!!!\n\nVOCÊ ESTA NO JOGO!")
    sala_pokebola()


# Segunda sala
def sala_pokemon(pokebola, doce):
    """Sala pokemon aqui vc pode capturar o pikachu se
    acalmar ele dando um doce."""
    print("AO ENTRAR NA SALA VOCE ESCUTA UM ROSNADO")
    print("VOCE SE VIRA PARA O ROSNADO VE UM PIKACHU",
            "MUITO BRAVO OLHANDO PARA VOCE.")
    print("O QUE VOCE FAZ??")

    pikachu = "BRAVO"

    while True:
        escolha = input("> ")

        if "CAPTURAR" in escolha and pokebola == 1 and pikachu == "BRAVO":
            print("VOCE LANCA A POKEBOLA E O PIKACHU REBATE A POKEBOLA.")
            derrota("PIKACHU USA CHOQUE DO TROVAO EM VOCE.")
        elif "CAPTURAR" in escolha and pokebola == 1 and pikachu == "CALMO":
            print("VOCE LANCA A POKEBOLA E CAPTURA O PIKACHU")
            print("VOCE PASSA PARA A PROXIMA SALA")
            vitoria("VOCE CAPTUROU O PIKACHU!!!!")
        elif "CAPTURAR" in escolha and pokebola == 0 and pikachu == "CALMO":
            derrota("VOCE NAO TEM POKEBOLA O PIKACHU USA RAIO EM VOCE.")
        elif "DOCE" in escolha and doce == 1:
            print("O PIKACHU ESTA TRANQUILAMENTE COMENDO O DOCE")
            pikachu = "CALMO"
        elif "DOCE" in escolha and doce == 0:
            derrota("VOCE NAO TEM DOCE PARA DAR PARA O " + 
                    "PIKACHU ELE USOU CHOQUE DO TROVAO EM VOCE.")
        else:
            derrota("PIKACHU TE ATACA, COM TERA VOLT.")


# Primeira sala. sala pokemon.
def sala_pokebola():
    """Sala onde o jogador pode pegar uma pokebola ou
    ir para outra sala"""
    print("VOCE ACORDOU EM UMA SALA.")
    print("NA SALA TEM UMA MESA E UMA PORTA.")
    print("O QUE VOCE FAZ?")
    
    escolha = input("> ")

    if "MESA" in escolha:
        print("NA MESA VOCÊ ENCONTRA UMA POKEBOLA E UM DOCE.")
        print("VOCE PEGA O DOCE E A POKEBOLA.")
        pokebola = 1
        doce = 1
    elif "PORTA":
        pokebola = 0
        doce = 0
    else: 
        derrota("VOCE FICOU PRESO NA SALA.")
    sala_pokemon(pokebola, doce)



# Inicio do jogo
def start():
    """inicio do jogo. escreve mensagem de boas vindas
    e leva para a primeira sala do jogo."""
    print("BEM VINDO!!!\n\nVOCÊ ESTA NO JOGO!")
    sala_pokebola()


if __name__ == '__main__':
    start()
