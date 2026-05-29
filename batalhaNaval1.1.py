# agua = '\U0001F30A'
# barco = '\U0001F6A2'
# desturido = '\U0001F4A5'
import random
while True:
    def Jogo():
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
        print('Tabuleiros')
        print('Tabuleiro do Jogador')
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                    TabulJog[i][j] = '\U0001F30A'
            print(f'{i} {TabulJog[i]}')
        print('------------------------------')
        print('Tabuleiro do Computador')
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                TabulComp[i][j] = '\U0001F30A'
            print(f'{i} {TabulComp[i]}')
        for i in range(5):
            ataqueLinha = int(input(f'Digite uma linha para o {i+1} ataque: '))
            ataqueColuna = int(input(f'Digite uma Coluna para o {i+1} ataque: '))
            if ataqueLinha and ataqueColuna == TabulComp[linha][coluna]:
                print('Você acertou uma embarcação')
                print('X    0     1     2     3     4     5     6     7     8     9')
                TabulComp[linha][coluna] = '\U0001F4A5'
                for i in range(10):
                    for j in range(10):
                        TabulComp[i][j] = '\U0001F30A'
                print(f'{i} {TabulComp[i]}')
            else:
                print('Você errou')
                print('X    0     1     2     3     4     5     6     7     8     9')
                for i in range(10):
                    for j in range(10):
                        TabulComp[i][j] = '\U0001F30A'
                    print(f'{i} {TabulComp[i]}')
        for i in range(5):
            ataqueLinha = random.randint(0,9)
            ataqueColuna = random.randint(0,9)
            if ataqueLinha and ataqueColuna == TabulJog[linha][coluna]:
                print('O computador acertou uma embarcação')
                print('X    0     1     2     3     4     5     6     7     8     9')
                TabulJog[linha][coluna] = '\U0001F4A5'
                for i in range(10):
                    for j in range(10):
                        TabulJog[i][j] = '\U0001F30A'
                print(f'{i} {TabulJog[i]}')
            else:
                print('Você errou')
                print('X    0     1     2     3     4     5     6     7     8     9')
                for i in range(10):
                    for j in range(10):
                        TabulJog[i][j] = '\U0001F30A'
                    print(f'{i} {TabulJog[i]}')
    print('Olá, bem vindo ao Batalha Naval!')
    print('Você quer jogar?\n1. Sim, jogar\n0. sair')
    jogo = int(input(''))
    if jogo == 0:
        break
    if jogo == 1:
        Jogo()