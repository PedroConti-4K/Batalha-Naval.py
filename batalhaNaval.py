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
    TabulAcertosJog = [
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
    TabulAcertosCom = [
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
    
    def imprimTabulAcertosJog():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if TabulAcertosJog[i][j] == 0:
                    TabulAcertosJog[i][j] = '\U0001F30A'
                if TabulAcertosJog[i][j] == 'X':
                    TabulAcertosJog[i][j] = '\U0001F4A5'
        for i in range(10):
            print(f'{i} {TabulAcertosJog[i]}')

    def imprimTabulAcertosCom():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if TabulAcertosCom[i][j] == 0:
                    TabulAcertosCom[i][j] = '\U0001F30A'
                if TabulAcertosCom[i][j] == 'X':
                    TabulAcertosCom[i][j] = '\U0001F4A5'
        for i in range(10):
            print(f'{i} {TabulAcertosCom[i]}')

    def imprimTabulJog():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if jogador[i][j] == 0:
                    jogador[i][j] = '\U0001F30A'
                if jogador[i][j] == 'O':
                    jogador[i][j] = '\U0001F6A2'
        for i in range(10):
            print(f'{i} {jogador[i]}')
        print('--------------------------------------------------------------')

    def imprimTabulCom():
        print('X    0     1     2     3     4     5     6     7     8     9')
        for i in range(10):
            for j in range(10):
                if computador[i][j] == 0:
                    computador[i][j] = '\U0001F30A'
                if computador[i][j] == 'O':
                    computador[i][j] = '\U0001F6A2'
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
        print('--------------------------------------------------------------')
        print('Tabuleiro do Jogador')
        imprimTabulAcertosJog()
        print('--------------------------------------------------------------')
        print('Tabuleiro do Computador')
        imprimTabulAcertosCom()
        print('--------------------------------------------------------------')
        print(f'ATAQUES!"\U0001F4A5"')
        acertosJog = 0
        acertosCom = 0
        i = 0
        while i <5:
            atqL = computador[linha]
            atqC = computador[coluna]
            atqL = int(input(f'Digite a linha do {i+1} ataque: '))
            atqC = int(input(f'Digite a coluna do {i+1} ataque: '))
            if computador[atqL][atqC] == '\U0001F6A2':
                TabulAcertosJog[atqL][atqC] = 'X'
                acertosJog +=1
                print('Você acertou uma embarcação')
                print('--------------------------------------------------------------')
            else:
                print('Você errou')
                print('--------------------------------------------------------------')
            print('Tabuleiro do Computador')
            imprimTabulAcertosJog()
            print('--------------------------------------------------------------')
            atqComL = jogador[linha]
            atqComC = jogador[coluna]
            atqComL = random.randint(0,9)
            print(f'O computador atacou a linha {atqComL}')
            atqComC = random.randint(0,9)
            print(f'O computador atacou a coluna {atqComC}')
            if jogador[atqComL][atqComC] == '\U0001F6A2':
                TabulAcertosCom[atqComL][atqComC] = 'X'
                acertosCom +=1
                print('O computador acertou uma embarcação')
                print('--------------------------------------------------------------')
            else:
                print('O computador errou')
                print('--------------------------------------------------------------')
            print('Tabuleiro do Jogador')
            imprimTabulAcertosCom()
            print('--------------------------------------------------------------')
            print('Placar')
            print(f'Jogador: {acertosJog}')
            print(f'Computador: {acertosCom}')
            print('--------------------------------------------------------------')
            i +=1
            if i == 5:
                print('Placar Final')
                print(f'O jogador acertou {acertosJog} embarcações')
                print(f'O Computador acertou {acertosCom} embarcações')
                print('--------------------------------------------------------------')
                print('Tabuleiro do Jogador')
                imprimTabulJog()
                print('Tabuleiro do Computador')
                imprimTabulCom()
                print('--------------------------------------------------------------')
                print('Desenvolvido por:\nLeo\nPedro\nRenan')
                print('--------------------------------------------------------------')
    print('Você quer jogar?\n1. Sim, jogar\n0. Não, sair')
    batNaval = int(input(''))
    if batNaval == 0:
        break
    if batNaval == 1:
        jogo()
