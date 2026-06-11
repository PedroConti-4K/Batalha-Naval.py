import random
import time
import os
import sys

NEUTRO = "\U00002B1C"
ACERTO = "\U0001F4A5"
AGUA   = "\U0001F30A"
NAVIO  = "\U0001F6F6" #🛶
SUBMARINO = "\U0001F6A4" #🚤
CONTRA_TORPEDEIRO = "\U000026F5" # ⛵
TANQUE = "\U000026F4" # ⛴
PORTA_AVIOES = "\U0001F6A2" #🚢

def limpar_tela():
    """Função para limpar o terminal ta guys"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_ataque():
    """Cria o efeito visual de 'Lançando ataque...' por tipo 2 segundos."""
    sys.stdout.write("Lançando ataque")
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(0.6)
        sys.stdout.write(".")
        sys.stdout.flush()
    time.sleep(0.2)

def criar_tabuleiro():
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(NEUTRO)
        tabuleiro.append(linha)
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, titulo):
    print(f"\n{titulo}")
    print("  0  1  2  3  4  5  6  7  8  9 ")
    for i in range(10):
        print(f"{i} ", end="")
        for j in range(10):
            print(tabuleiro[i][j], end=" ")
        print()
    print('--------------------------------')

def posicionar_navios_jogador(secreto_jogador):
    print("\nPosicione suas 5 embarcações!")
    i = 0
    while i <1:
        # Navio
        mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro\n ")
        Navio_linha = input("Digite a linha para o Navio (0-9): ")
        if not Navio_linha.isdigit():
            print("Digite apenas números!")
            continue
        Navio_linha = int(Navio_linha)
        if Navio_linha < 0 or Navio_linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        
        Navio_coluna = input("Digite a coluna para o Navio (0-9): ")
        if not Navio_coluna.isdigit():
            print("Digite apenas números!")
            continue
        Navio_coluna = int(Navio_coluna)
        if Navio_coluna < 0 or Navio_coluna > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        if secreto_jogador[Navio_linha][Navio_coluna] != NEUTRO:
            print("Já tem uma embarcação aí! Escolha outra posição.")
            continue
        secreto_jogador[Navio_linha][Navio_coluna] = NAVIO
        mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro\n ")
        
        # Submarino
        Submarino_linha = input("Digite a linha para o Submarino (0-9): ")
        if not Submarino_linha.isdigit():
            print("Digite apenas números!")
            continue
        Submarino_linha = int(Submarino_linha)
        if Submarino_linha < 0 or Submarino_linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        
        Submarino_coluna = input("Digite a coluna para o Submarino (0-8): ")
        if not Submarino_coluna.isdigit():
            print("Digite apenas números!")
            continue
        Submarino_coluna = int(Submarino_coluna)
        if Submarino_coluna < 0 or Submarino_coluna > 8:
            print("Coordenada inválida! Digite um número entre 0 e 8.")
            continue
        for i in range(2):
            if secreto_jogador[Submarino_linha][Submarino_coluna+i] != NEUTRO:
                print("Já tem uma embarcação aí! Escolha outra posição.")
                continue
        for i in range(2):
            secreto_jogador[Submarino_linha][Submarino_coluna+i] = SUBMARINO
            mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro\n ")

        # Torpedeiro
        Torpedeiro_linha = input("Digite a linha para o Contra-Torpedeiro (0-9): ")
        if not Torpedeiro_linha.isdigit():
            print("Digite apenas números!")
            continue
        Torpedeiro_linha = int(Torpedeiro_linha)
        if Torpedeiro_linha < 0 or Torpedeiro_linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        
        Torpedeiro_coluna = input("Digite a coluna para o Contra-Torpedeiro (0-7): ")
        if not Torpedeiro_coluna.isdigit():
            print("Digite apenas números!")
            continue
        Torpedeiro_coluna = int(Torpedeiro_coluna)
        if Torpedeiro_coluna < 0 or Torpedeiro_coluna > 7:
            print("Coordenada inválida! Digite um número entre 0 e 7.")
            continue
        for i in range(3):
            if secreto_jogador[Torpedeiro_linha][Torpedeiro_coluna+i] != NEUTRO:
                print("Já tem uma embarcação aí! Escolha outra posição.")
                continue
        for i in range(3):
            secreto_jogador[Torpedeiro_linha][Torpedeiro_coluna+i] = CONTRA_TORPEDEIRO
            mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro\n ")

        # Tanque
        Tanque_linha = input("Digite a linha para o Navio-Tanque (0-9): ")
        if not Tanque_linha.isdigit():
            print("Digite apenas números!")
            continue
        Tanque_linha = int(Tanque_linha)
        if Tanque_linha < 0 or Tanque_linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        
        Tanque_coluna = input("Digite a coluna para o Navio-Tanque (0-6): ")
        if not Tanque_coluna.isdigit():
            print("Digite apenas números!")
            continue
        Tanque_coluna = int(Tanque_coluna)
        if Tanque_coluna < 0 or Tanque_coluna > 6:
            print("Coordenada inválida! Digite um número entre 0 e 6.")
            continue
        
        for i in range(4):
            if secreto_jogador[Tanque_linha][Tanque_coluna+i] != NEUTRO:
                print("Já tem uma embarcação aí! Escolha outra posição.")
                continue
        for i in range(4):
            secreto_jogador[Tanque_linha][Tanque_coluna+i] = TANQUE
            mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro\n ")

        # Porta Aviões
        Porta_linha = input("Digite a linha para o Porta-Aviões (0-9): ")
        if not Porta_linha.isdigit():
            print("Digite apenas números!")
            continue
        Porta_linha = int(Porta_linha)
        if Porta_linha < 0 or Porta_linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue
        
        Porta_coluna = input("Digite a coluna para o Porta-Aviões (0-5): ")
        if not Porta_coluna.isdigit():
            print("Digite apenas números!")
            continue
        Porta_coluna = int(Porta_coluna)
        if Porta_coluna < 0 or Porta_coluna > 5:
            print("Coordenada inválida! Digite um número entre 0 e 5.")
            continue
        for i in range(5):
            if secreto_jogador[Porta_linha][Porta_coluna+i] != NEUTRO:
                print("Já tem uma embarcação aí! Escolha outra posição.")
                continue
        for i in range(5):
            secreto_jogador[Porta_linha][Porta_coluna+i] = PORTA_AVIOES

        print(f"Embarcações posicionadas!")

        i +=1
        time.sleep(1)
        limpar_tela()

    mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro final, boa sorte!")

def posicionar_navios_pc(secreto_pc):
    i = 0
    while i < 1:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        
        if secreto_pc[linha][coluna] != NEUTRO:
            continue
        
        secreto_pc[linha][coluna] = NAVIO

        # Submarino
        submarino_linha = random.randint(0, 9)
        submarino_coluna = random.randint(0, 8)

        for i in range(2):
            if secreto_pc[submarino_linha][submarino_coluna+i] != NEUTRO:
                continue
        for i in range(2):
            secreto_pc[submarino_linha][submarino_coluna+i] = SUBMARINO

        # Torpedeiro
        torpedeiro_linha = random.randint(0, 9)
        torpedeiro_coluna = random.randint(0, 7)

        for i in range(3):
            if secreto_pc[torpedeiro_linha][torpedeiro_coluna+i] != NEUTRO:
                continue
        for i in range(3):
            secreto_pc[torpedeiro_linha][torpedeiro_coluna+i] = CONTRA_TORPEDEIRO

        # Tanque
        tanque_linha = random.randint(0, 9)
        tanque_coluna = random.randint(0, 6)

        for i in range(4):
            if secreto_pc[tanque_linha][tanque_coluna+i] != NEUTRO:
                continue
        for i in range(4):
            secreto_pc[tanque_linha][tanque_coluna+i] = TANQUE

        # Porta_Avioes
        porta_linha = random.randint(0, 9)
        porta_coluna = random.randint(0, 5)

        for i in range(5):
            if secreto_pc[porta_linha][porta_coluna+i] != NEUTRO:
                continue
        for i in range(5):
            secreto_pc[porta_linha][porta_coluna+i] = PORTA_AVIOES

        i +=1

def atacar(linha,coluna,secreto_alvo,visivel_alvo):
    if visivel_alvo[linha][coluna] == ACERTO or visivel_alvo[linha][coluna] == AGUA:
        return "repetido"
    elif secreto_alvo[linha][coluna] == NAVIO:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    elif secreto_alvo[linha][coluna] == SUBMARINO:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    elif secreto_alvo[linha][coluna] == CONTRA_TORPEDEIRO:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    elif secreto_alvo[linha][coluna] == TANQUE:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    elif secreto_alvo[linha][coluna] == PORTA_AVIOES:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    else:
        visivel_alvo[linha][coluna] = AGUA
        return "erro"

def turno_jogador(secreto_pc,visivel_pc,visivel_jogador):
    print(f"É sua vez de atacar, escolha a posição do tabuleiro adversário ")
    while(True):
        linha = input("Digite a linha (0-9): ")
        if not linha.isdigit():
            print("Digite apenas números!")
            continue
        linha = int(linha)
        if linha < 0 or linha > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue

        coluna = input("Digite a coluna (0-9): ") 
        if not coluna.isdigit():
            print("Digite apenas números!")
            continue
        coluna = int(coluna)
        if coluna < 0 or coluna > 9:
            print("Coordenada inválida! Digite um número entre 0 e 9.")
            continue

        limpar_tela()
        animacao_ataque()
        limpar_tela()

        resultado = atacar(linha,coluna,secreto_pc,visivel_pc)
        if resultado == "repetido":
            print("Essa posição já foi atacada, mais atenção")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            continue
        elif resultado == "acerto":
            print("Parabéns, você encontrou e destruiu uma embarcação")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            break
        elif resultado == "erro":
            print("Que pena, seu ataque foi na água")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            break
        
def turno_computador(secreto_jogador, visivel_jogador, visivel_pc):
    limpar_tela()
    print("Vez do Computador")
    time.sleep(1.5)
    animacao_ataque()
    limpar_tela()

    while(True):
        ataquelinha = random.randint(0,9)
        ataquecoluna = random.randint(0,9)
        ataque = atacar(ataquelinha,ataquecoluna,secreto_jogador,visivel_jogador)

        if ataque == "repetido":
            continue
        elif ataque == "acerto":
            print("O computador acertou uma embarcação sua!")
            time.sleep(1)
            print(f"A embarcação da linha {ataquelinha} e coluna {ataquecoluna} foi destruída")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_jogador, "Tabuleiro do Jogador")
            break
        elif ataque == "erro":
            print("O computador errou seu ataque")
            time.sleep(1)
            print(f"O computador atacou a linha {ataquelinha} e a coluna {ataquecoluna}")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_jogador, "Tabuleiro do Jogador")
            break
            
def verificar_vitoria(visivel):
    acertos = 0
    for i in range(10):
        for j in range(10):
            if visivel[i][j] == ACERTO:
                acertos += 1
    return acertos == 15

def main():
    limpar_tela()
    print("Bem vindo ao jogo de Batalha Naval")
    secreto_jogador = criar_tabuleiro()
    secreto_pc = criar_tabuleiro()
    visivel_jogador = criar_tabuleiro()
    visivel_pc = criar_tabuleiro()

    posicionar_navios_jogador(secreto_jogador)
    posicionar_navios_pc(secreto_pc)

    time.sleep(10)
    limpar_tela()
    mostrar_tabuleiro(visivel_jogador,"Tabuleiro do Jogador")
    mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")

    while True:
        turno_jogador(secreto_pc, visivel_pc, visivel_jogador)
        if verificar_vitoria(visivel_pc):
            print("Parabéns! Você afundou toda a frota inimiga!")
            mostrar_tabuleiro(visivel_jogador,"Tabuleiro do Jogador")
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            print("Obrigado por jogar!")
            print("Desenvolvido por:\nLeo Takano\nPedro Henrique\nRenan Nascimento")
            break

        time.sleep(4)

        turno_computador(secreto_jogador, visivel_jogador, visivel_pc)
        if verificar_vitoria(visivel_jogador):
            print("O computador afundou toda a sua frota! Você perdeu!")
            mostrar_tabuleiro(visivel_jogador,"Tabuleiro do Jogador")
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            print("Obrigado por jogar!")
            print("Desenvolvido por:\nLeo Takano\nPedro Henrique\nRenan Nascimento")
            break
        time.sleep(7)
        limpar_tela()
main()
