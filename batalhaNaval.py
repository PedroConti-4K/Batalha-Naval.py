# agua = '\U0001F30A'
# barco = '\U0001F6A2'
# desturido = '\U0001F4A5'
import random
print('Olá, bem vindo ao Batalha Naval!')
while True:
    jogador = [
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
    computador = [
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
    TabulPadrao = [
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
    def imprimTabulPadrao():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                TabulPadrao[i][j] = '\U0001F30A'
        for i in range(10):
            print(f'{i} {TabulPadrao[i]}')

    def imprimTabulJog():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if jogador[i][j] == 0:
                    jogador[i][j] = '\U0001F30A'
                if jogador[i][j] == 'X':
                    jogador[i][j] = '\U0001F4A5'
        for i in range(10):
            print(f'{i} {jogador[i]}')
        print('--------------------------------------------------------------')

    def imprimTabulCom():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if computador[i][j] == 0:
                    computador[i][j] = '\U0001F30A'
                if computador[i][j] == 'X':
                    computador[i][j] = '\U0001F4A5'
        for i in range(10):
            print(f'{i} {computador[i]}')

    def jogo():
        print('Tabuleiro do Jogo')
        imprimTabulJog()
        for i in range(5):
            linha = int(input(f'Digite a linha da {i+1} embarcação: '))
            coluna = int(input(f'Digite a coluna da {i+1} embarcação: '))
            jogador[linha][coluna] = 'O'
        for i in range(5):
            linha = random.randint(0,9)
            coluna = random.randint(0,9)
            computador[linha][coluna] = 'O'
        # imprimTabulJog()
        print('--------------------------------------------------------------')
        print('Tabuleiro do Jogardor')
        imprimTabulPadrao()
        print('--------------------------------------------------------------')
        print('Tabuleiro do Computador')
        imprimTabulPadrao()
        print('--------------------------------------------------------------')
        print(f'ATAQUES!"\U0001F4A5"')
        for i in range(5):
            atqJogLinha = int(input(f'Digite uma linha para o {i+1} ataque: '))
            atqJogColuna = int(input(f'Digite uma Coluna para o {i+1} ataque: '))
            if (atqJogLinha and atqJogColuna) == (computador[linha][coluna] == 'O'):
                computador[linha][coluna] = 'X'
                print('Você acertou uma embracação')
                print('Tabuleiro do Computador')
                imprimTabulCom()
                print('--------------------------------------------------------------')
            atqComLinha = random.randint(0,9)
            atqComColuna = random.randint(0,9)
            if (atqComLinha and atqComColuna) == (jogador[linha][coluna] == 'O'):
                jogador[linha][coluna] = 'X'
                print('O computador acertou uma embracação')
                print('Tabuleiro do Jogador')
                imprimTabulJog()
    print('Você quer jogar?\n1. Sim, jogar\n0. sair')
    batNaval = int(input(''))
    if batNaval == 0:
        break
    if batNaval == 1:
        jogo()