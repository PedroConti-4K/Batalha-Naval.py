# agua = '\U0001F30A'
# barco = '\U0001F6A2'
import random
while True:
    def TabulDeJogo():
        TabulJog = [
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
        TabulComp = [
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
        print('Tabuleiro do Jogo')
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                TabulJog[i][j] = '\U0001F30A'
            print(f'{i} {TabulJog[i]}')
        print('------------------------------')
        for i in range(5):
            linha = int(input(f'Digite a linha da {i+1} embarcação: '))
            coluna = int(input(f'Digite a coluna da {i+1} embarcação: '))
            TabulJog[linha][coluna] = 'X'
        for j in range(5):
            linha = random.randint(0,9)
            coluna = random.randint(0,9)
            TabulComp[linha][coluna] = 'X'
        print('------------------------------')
        for i in range(10):
            for j in range(10):
                if TabulJog[i][j] == 'X':
                    TabulJog[i][j] = '\U0001F6A2'
                else:
                    TabulJog[i][j] = '\U0001F30A'
            print(TabulJog[i])

    print('Olá, bem vindo ao Batalha Naval!')
    print('Você quer jogar?\n1. Sim, jogar\n0. sair')
    jogo = int(input(''))
    if jogo == 0:
        break
    if jogo == 1:
        TabulDeJogo()