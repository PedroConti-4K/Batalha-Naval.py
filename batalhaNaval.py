# agua = '\U0001F30A' emoji começa com \U e preenchido com 0s até ter 8 números após o U
# link dos emojis = https://www.unicode.org/emoji/charts/full-emoji-list.html?hl=pt-br#1f30a
import random
print('Olá, bem vindo ao Batalha Naval!')
# while True:
tabuleiroComp = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
tabuleiroJog = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
print('Você quer jogar?\n1. Sim, jogar\n0. sair')
jogo = int(input(''))
# Validação do jogo
# if jogo ==0:
    # break
if jogo ==1:
    print('Tabuleiro do Computador')
    for linha in range(10):
        for coluna in range(10):
            tabuleiroComp[linha][coluna] = '\U0001F30A'
        print(tabuleiroComp[linha])
    print('------------------------------')
    print('Tabuleiro do Jogador')
    for linha in range(10):
        for coluna in range(10):
            tabuleiroJog[linha][coluna] = '\U0001F30A'
        print(tabuleiroJog[linha])
    print('------------------------------')