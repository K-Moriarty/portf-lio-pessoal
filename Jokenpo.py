from random import randint
from time import sleep
import os 

itens = ("Pedra", "Papel", "Tesoura")
single_player = "Jogador vs computador"
multiplayer = "2 Jogadores"

modo_de_jogo = input(f"Escolha o seu modo de jogo, insira (s) para {single_player}, (m) para {multiplayer}: ")

if modo_de_jogo == 's':
    print(""" Seja Bem-vindo ao modo single player! Suas opções são:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")
    
    jogador = int(input("Qual é a sua jogada? "))
    computador = randint(0, 2)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    print("-=" * 11)
    print("Computador jogou {}".format(itens[computador]))
    print("Jogador jogou {}".format(itens[jogador]))
    print("-=" * 11)
    
    if computador == 0:
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR VENCE")
        elif jogador == 2:
            print("COMPUTADOR VENCE")
        else:
            print("JOGADA INVÁLIDA!")
    elif computador == 1:
        if jogador == 0:
            print("COMPUTADOR VENCE")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR VENCE")
        else:
            print("JOGADA INVÁLIDA!")
    elif computador == 2:
        if jogador == 0:
            print("JOGADOR VENCE")
        elif jogador == 1:
            print("COMPUTADOR VENCE")
        elif jogador == 2:
            print("EMPATE")
        else:
            print("JOGADA INVÁLIDA!")
            
            
elif modo_de_jogo == 'm':
    jogador1 = input("Digite o seu nome (jogador1): ")
    jogador2 = input("Digite o seu nome (jogador2): ")
    
pontuacao1 = 0
pontuacao2 = 0
empate = 0
historico_jogadas = ""
historico_resultados = ""
rodadas = 1

if modo_de_jogo == 'm':
     print(""" Seja Bem-vindo ao modo multiplayer! Suas opções são:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")
    
jogador1 = int(input("Qual é a sua jogada? "))
os.system('cls' if os.name == 'nt' else 'clear')
print(""" Suas opções são:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")

jogador2 = int(input("Qual é a sua jogada? "))
os.system('cls' if os.name == 'nt' else 'clear')
print(""" Suas opções são:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=" * 11)
print("jogador1 jogou {}".format(itens[jogador1]))
print("jogador2 jogou {}".format(itens[jogador2]))
print("-=" * 11)

if jogador2 == 0:
        if jogador1 == 0:
            print("EMPATE")
        elif jogador1 == 1:
            print("jogador1 VENCE")
        elif jogador1 == 2:
            print("jogador2 VENCE")
        else:
            print("JOGADA INVÁLIDA!")
elif jogador2 == 1:
        if jogador1 == 0:
            print("jogador2 VENCE")
        elif jogador1 == 1:
            print("EMPATE")
        elif jogador1 == 2:
            print("jogador1 VENCE")
        else:
            print("JOGADA INVÁLIDA!")
elif jogador2 == 2:
        if jogador1 == 0:
            print("jogador1 VENCE")
        elif jogador1 == 1:
            print("jogador2 VENCE")
        elif jogador1 == 2:
            print("EMPATE")
        else:
            print("JOGADA INVÁLIDA!")
