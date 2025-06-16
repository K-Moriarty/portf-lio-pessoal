import random
import time
import os

#Funcao para limpar a tela
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Funcao para criar um tabuleiro vazio
def criar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append('~')
        tabuleiro.append(linha)
    return tabuleiro

#Funcao para mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro, mostrar_navios):
    letras = ""
    for i in range(len(tabuleiro)):
        letras += chr(65 + i) + " "
    print("   " + letras)
    for i in range(len(tabuleiro)):
        linha = ""
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == 'N' and not mostrar_navios:
                linha += '~ '
            else:
                linha += tabuleiro[i][j] + " "
        print(f"{i+1:2} {linha}")

#Funcao para posicionar navios manualmente
def posicionar_navios(tabuleiro, lista_navios, nome):
    print(f"\n{nome}, posicione seus navios!")
    for navio in lista_navios:
        for tentativa in range(3):  #3 tentativas por navio
            print(f"\nNavio: {navio['nome']} ({navio['tamanho']} casas)")
            try:
                col = input("Coluna inicial (A, B, C...): ").upper()
                lin = int(input("Linha inicial (1, 2, 3...): ")) - 1
                ori = input("Orientacao (H para horizontal, V para vertical): ").upper()
                col_num = ord(col) - 65
                if ori == "H":
                    if col_num + navio["tamanho"] <= len(tabuleiro):
                        sobrepoe = False
                        for c in range(col_num, col_num + navio["tamanho"]):
                            if tabuleiro[lin][c] == 'N':
                                sobrepoe = True
                        if not sobrepoe:
                            for c in range(col_num, col_num + navio["tamanho"]):
                                tabuleiro[lin][c] = 'N'
                            break
                elif ori == "V":
                    if lin + navio["tamanho"] <= len(tabuleiro):
                        sobrepoe = False
                        for l in range(lin, lin + navio["tamanho"]):
                            if tabuleiro[l][col_num] == 'N':
                                sobrepoe = True
                        if not sobrepoe:
                            for l in range(lin, lin + navio["tamanho"]):
                                tabuleiro[l][col_num] = 'N'
                            break
                print("Posicao invalida ou sobreposicao! Tente de novo.")
            except:
                print("Entrada invalida! Tente de novo.")

#Funcao para posicionar navios aleatoriamente
def posicionar_navios_aleatorio(tabuleiro, lista_navios):
    for navio in lista_navios:
        colocado = False
        for tentativa in range(20):
            lin = random.randint(0, len(tabuleiro)-1)
            col = random.randint(0, len(tabuleiro)-1)
            ori = random.choice(["H", "V"])
            if ori == "H":
                if col + navio["tamanho"] <= len(tabuleiro):
                    sobrepoe = False
                    for c in range(col, col + navio["tamanho"]):
                        if tabuleiro[lin][c] == 'N':
                            sobrepoe = True
                    if not sobrepoe:
                        for c in range(col, col + navio["tamanho"]):
                            tabuleiro[lin][c] = 'N'
                        break
            else:
                if lin + navio["tamanho"] <= len(tabuleiro):
                    sobrepoe = False
                    for l in range(lin, lin + navio["tamanho"]):
                        if tabuleiro[l][col] == 'N':
                            sobrepoe = True
                    if not sobrepoe:
                        for l in range(lin, lin + navio["tamanho"]):
                            tabuleiro[l][col] = 'N'
                        break

#Funcao para realizar um ataque
def atacar(tabuleiro, tab_ataque, nome):
    print(f"\nVez de {nome} atacar!")
    for tentativa in range(3):  #3 tentativas para acertar uma coordenada valida
        try:
            col = input("Coluna do ataque: ").upper()
            lin = int(input("Linha do ataque: ")) - 1
            col_num = ord(col) - 65
            if tab_ataque[lin][col_num] != '~':
                print("Voce ja atacou aqui! Tente outra coordenada.")
            else:
                if tabuleiro[lin][col_num] == 'N':
                    print("Acertou um navio!")
                    tab_ataque[lin][col_num] = 'X'
                    tabuleiro[lin][col_num] = 'X'
                    return "acerto"
                else:
                    print("Errou, so agua.")
                    tab_ataque[lin][col_num] = 'O'
                    tabuleiro[lin][col_num] = 'O'
                    return "erro"
        except:
            print("Coordenada invalida! Tente de novo.")
    return "erro"

#Ataque aleatorio do Computador
def ataque_pc(tabuleiro, tab_ataque):
    for tentativa in range(20):
        lin = random.randint(0, len(tabuleiro)-1)
        col = random.randint(0, len(tabuleiro)-1)
        if tab_ataque[lin][col] == '~':
            print(f"PC atacou {chr(65+col)}{lin+1}")
            time.sleep(2)
            if tabuleiro[lin][col] == 'N':
                print("PC acertou um navio!")
                tab_ataque[lin][col] = 'X'
                tabuleiro[lin][col] = 'X'
                return "acerto"
            else:
                print("PC errou, so agua.")
                tab_ataque[lin][col] = 'O'
                tabuleiro[lin][col] = 'O'
                return "erro"
    return "erro"

#Verifica se todos os navios foram afundados
def todos_afundados(tabuleiro):
    for linha in tabuleiro:
        for cel in linha:
            if cel == 'N':
                return False
    return True

#Funcao principal do jogo
def jogo():
    print("="*30)
    print("BATALHA NAVAL".center(30))
    print("="*30)
    try:
        tamanho = int(input("Tamanho do tabuleiro (min 10): "))
        if tamanho < 10:
            tamanho = 10
    except:
        tamanho = 10

    print("\n1 - Jogador vs Jogador\n2 - Jogador vs PC")
    modo = input("Escolha o modo: ")
    if modo == "1":
        nome1 = input("Nome do Jogador 1: ")
        nome2 = input("Nome do Jogador 2: ")
    else:
        nome1 = input("Seu nome: ")
        nome2 = "PC"

    #Definicao dos navios
    lista_navios = [
        {"nome":"Encouracado", "tamanho":5},
        {"nome":"Porta-avioes", "tamanho":4},
        {"nome":"Contratorpedeiro", "tamanho":3},
        {"nome":"Contratorpedeiro", "tamanho":3},
        {"nome":"Submarino", "tamanho":2},
        {"nome":"Submarino", "tamanho":2}
    ]

    #Criar tabuleiros
    tab1 = criar_tabuleiro(tamanho)
    tab2 = criar_tabuleiro(tamanho)
    tab_ataque1 = criar_tabuleiro(tamanho)
    tab_ataque2 = criar_tabuleiro(tamanho)

    #Posicionar navios
    posicionar_navios(tab1, lista_navios, nome1)
    if modo == "1":
        posicionar_navios(tab2, lista_navios, nome2)
    else:
        posicionar_navios_aleatorio(tab2, lista_navios)

    #Estatisticas
    tiros1 = 0
    acertos1 = 0
    tiros2 = 0
    acertos2 = 0

    #Loop de turnos
    for rodada in range(200):  #Limite grande de rodadas
        limpar_tela()
        print(f"\nRodada {rodada+1}")
        #Turno do Jogador 1
        mostrar_tabuleiro(tab_ataque1, False)
        resultado = atacar(tab2, tab_ataque1, nome1)
        tiros1 += 1
        if resultado == "acerto":
            acertos1 += 1
        if todos_afundados(tab2):
            print(f"\n{name1} venceu!")
            break

        #Turno do Jogador 2 ou Computador
        if modo == "1":
            mostrar_tabuleiro(tab_ataque2, False)
            resultado = atacar(tab1, tab_ataque2, nome2)
        else:
            resultado = ataque_pc(tab1, tab_ataque2)
        tiros2 += 1
        if resultado == "acerto":
            acertos2 += 1
        if todos_afundados(tab1):
            print(f"\n{name2} venceu!")
            break

    #Estatisticas finais
    print("\n=== ESTATISTICAS ===")
    print(f"{nome1}: Tiros: {tiros1} | Acertos: {acertos1}")
    print(f"{nome2}: Tiros: {tiros2} | Acertos: {acertos2}")

#Iniciar o jogo
jogo()
