import random
import time
import os
import sys

NEUTRO = "\U00002B1C"
NAVIO  = "\U0001F6A2"
ACERTO = "\U0001F4A5"
AGUA   = "\U0001F30A"

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

def posicionar_navios_jogador(secreto_jogador):
    print("\nPosicione suas 5 embarcações!")
    
    navios = 0
    while navios < 5:
        mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro")
        
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
        if secreto_jogador[linha][coluna] == NAVIO:
            print("Já tem uma embarcação aí! Escolha outra posição.")
            continue
        
        secreto_jogador[linha][coluna] = NAVIO
        navios += 1
        print(f"Embarcação {navios} de 5 posicionada!")
        time.sleep(1)
        limpar_tela()

    mostrar_tabuleiro(secreto_jogador, "Seu tabuleiro final, boa sorte!")

def posicionar_navios_pc(secreto_pc):
    navios = 0
    while navios < 5:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        
        if secreto_pc[linha][coluna] == NAVIO:
            continue
        
        secreto_pc[linha][coluna] = NAVIO
        navios += 1

def atacar(linha,coluna,secreto_alvo,visivel_alvo):
    if visivel_alvo[linha][coluna] == ACERTO or visivel_alvo[linha][coluna] == AGUA:
        return "repetido"
    elif secreto_alvo[linha][coluna] == NAVIO:
        visivel_alvo[linha][coluna] = ACERTO
        return "acerto"
    else:
        visivel_alvo[linha][coluna] = AGUA
        return "erro"

def turno_jogador(secreto_pc,visivel_pc,visivel_jogador):
    print('--------------------------------------------------------------')
    print("É sua vez de atacar, escolha a posição do tabuleiro adversário ")
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
            print("Parabéns, você encontrou e destruiu uma embarcação!")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            break
        elif resultado == "erro":
            print("Que pena, seu ataque foi na água.")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
            break

def turno_computador(secreto_jogador, visivel_jogador, visivel_pc):
    limpar_tela()
    print("Vez do computador!")
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
            print(f"O navio da linha {ataquelinha} e coluna {ataquecoluna} foi destruído.")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_jogador, "Tabuleiro do Jogador")
            break
        elif ataque == "erro":
            print("O computador errou seu ataque.")
            time.sleep(1)
            print(f"Ataque do computador: linha {ataquelinha} e coluna {ataquecoluna}")
            time.sleep(1.5)
            mostrar_tabuleiro(visivel_jogador, "Tabuleiro do Jogador")
            break
            
def verificar_vitoria(visivel):
    acertos = 0
    for i in range(10):
        for j in range(10):
            if visivel[i][j] == ACERTO:
                acertos += 1
    return acertos == 5

def main():
    limpar_tela()
    print("Bem vindo ao jogo de Batalha Naval")
    secreto_jogador = criar_tabuleiro()
    secreto_pc = criar_tabuleiro()
    visivel_jogador = criar_tabuleiro()
    visivel_pc = criar_tabuleiro()
    
    posicionar_navios_jogador(secreto_jogador)
    posicionar_navios_pc(secreto_pc)
    
    time.sleep(3)
    limpar_tela()
    mostrar_tabuleiro(visivel_jogador,"Tabuleiro do Jogador")
    mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")
    
    while True:
        turno_jogador(secreto_pc, visivel_pc, visivel_jogador)
        if verificar_vitoria(visivel_pc):
            print("\nParabéns! Você afundou toda a frota inimiga!")
            print("Obrigado por jogar!")
            print("Jogo Desenvolvido por Leo Takano, Pedro Henrique e Renan Nascimento")
            break
            
        time.sleep(4)
        
        turno_computador(secreto_jogador, visivel_jogador, visivel_pc)
        if verificar_vitoria(visivel_jogador):
            print("\nO computador afundou toda a sua frota! Você perdeu!")
            print("Obrigado por jogar!")
            print("Jogo Desenvolvido por:\nLeo Takano\nPedro Henrique\nRenan Nascimento")
            break
            
        time.sleep(4)
        limpar_tela()
        mostrar_tabuleiro(visivel_jogador, "Tabuleiro do Jogador")
        mostrar_tabuleiro(visivel_pc, "Tabuleiro do Computador")

main()
