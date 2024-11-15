#imports
from collections import namedtuple
from itertools import product
import random

#CLASSES
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.pontos = 0
      
        
#VARIAVEIS
Carta = namedtuple('Carta', ['cor', 'numero'])
cores = {'a', 'v', 'm', 'd'}  # 'a' = azul, 'v' = vermelha, 'm' = amarela, 'd' = verde
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    
baralho = [Carta(cor, numero) for cor, numero in product(cores, numeros)]
    #print('Seu baralho possui', len(baralho), 'cartas')
random.shuffle(baralho)
    #print(baralho)  



#FUNCOES
#Escolher quem começa jogando 
def par_impar(jogadores):
    print(f"{jogadores[0].nome} escolhe Par ou Ímpar (P/I):")
    escolha = input().strip().upper()
    
    # Verifica se a escolha é válida, caso contrário, dá uma mensagem de erro e não entra em loop
    while escolha not in {"P", "I"}:
        print("Escolha inválida. Por favor, escolha entre P (Par) ou I (Ímpar).")
        escolha = input().strip().upper()

    resultado = random.randint(1, 10)
    print(f"Número sorteado: {resultado}")
    vencedor = jogadores[0] if (resultado % 2 == 0 and escolha == "P") or (resultado % 2 == 1 and escolha == "I") else jogadores[1]
    print(f"{vencedor.nome} começa jogando!")
    return vencedor

def inicio_turno (jogadores):
    print('Jogador que ira iniciar a partida: ')
    return par_impar(jogadores)

def mostrar_mao(jogador_atual):
    print(f"Cartas de {jogador_atual.nome}:")
    for idx, carta in enumerate(jogador_atual.mao):
        print(f"{idx}: {carta.cor} {carta.numero}")


    # Função para distribuir cartas
def distribui_carta(baralho, quantidade=5):
    dist = random.sample(baralho, quantidade)
    for carta in dist:
        baralho.remove(carta)
    return dist

    #Pescar uma carta do baralho
def pegar_carta(baralho, jogador, quantidade=1):
    dist = random.sample(baralho, quantidade)
    jogador.mao.extend(dist)  
    for carta in dist:
        baralho.remove(carta)  
    return dist

    # Função para o jogador escolher uma carta
def escolher_carta(jogador, carta_mesa):
    while True:
        print(f"\nMão de {jogador.nome}:")
        for idx, carta in enumerate(jogador.mao):
            print(f"{idx}: {carta.cor} {carta.numero}") 

        try:
            escolha = int(input(f"\n{jogador.nome}, escolha a carta que deseja jogar (0 a {len(jogador.mao) - 1}) ou 100 para passar a vez: "))

            if escolha == 100:
                print(f"{jogador.nome} passou a vez.")
                return None
            elif 0 <= escolha < len(jogador.mao):
                carta_escolhida = jogador.mao.pop(escolha)
                if carta_escolhida.cor == carta_mesa.cor or carta_escolhida.numero == carta_mesa.numero:
                    print(f"\n{jogador.nome} jogou: {carta_escolhida.cor} {carta_escolhida.numero}")
                    return carta_escolhida  
                else:
                    print("Escolha inválida. A carta precisa ter a mesma cor ou número da carta na mesa.")
                    jogador.mao.append(carta_escolhida) 
            else:
                print("Escolha inválida. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número correspondente ao índice da carta.")

            
def pegar_ultima_carta(jogador, baralho, carta_mesa):
    if baralho:
        ultima_carta = baralho.pop()  # Pega a última carta do baralho
        jogador.mao.append(ultima_carta)  # Adiciona à mão do jogador
        print(f'A carta retirada do baralho é: {ultima_carta}')
        carta_escolhida = escolher_carta(jogador, carta_mesa) 
        return carta_escolhida
    else:
        print("O baralho está vazio!")
        return None
    

def passar_vez(jogadores, indice_jogador):
    jogador_atual = jogadores[indice_jogador]
    print(f"\n{jogador_atual.nome} passou a vez.")
    indice_jogador = (indice_jogador + 1) % len(jogadores)
    return indice_jogador

def turno(jogador, baralho, carta_mesa, jogadores, indice_jogador):
    mostrar_mao(jogador) 
    print(f"\nÉ a vez de {jogador.nome}. Carta na mesa: {carta_mesa}")
    
    while True:
        print("Escolha sua ação:")
        print("1 - Escolher uma carta de sua mão.")
        print("2 - Pegar uma carta do baralho.")
        print("3 - Passar a vez.")
        
        escolha = input("Digite o número da sua escolha: ")
        if escolha == '1':
            carta_jogada = escolher_carta(jogador, carta_mesa)
            if carta_jogada:
                return carta_jogada 
        elif escolha == '2':
            pegar_carta(baralho, jogador)
            print(f"{jogador.nome} pegou uma carta.")
        elif escolha == '3':
            print(f"{jogador.nome} passou a vez.")
            return None 
        else:
            print("Escolha inválida. Tente novamente.")

            
def pontos_partida(jogadores):
    for jogador in jogadores:
        pontos = sum(carta.numero for carta in jogador.mao)
        print(f"{jogador.nome} tem {pontos} pontos.")


#LOGICA JOGO
    # Apresentação do jogo e criação dos jogadores
print('---------<<<<<-----------Que   os   Jogos   Comecem---------->>>>>>-----------------')
nome1 = input('Digite o nome do jogador 1: ')
nome2 = input('Digite o nome do jogador 2: ')
jogador1 = Jogador(nome1)
jogador2 = Jogador(nome2)
jogadores = [jogador1, jogador2]
indice_jogador = 0

# Escolhendo quem começa
#par_impar(jogadores)

# Distribuindo cartas iniciais para os jogadores
jogador1.mao = distribui_carta(baralho)
jogador2.mao = distribui_carta(baralho)
carta_mesa = distribui_carta(baralho, 1)[0]
print(f"\n----------Primeira carta aberta na mesa:{carta_mesa}----------------")


# Exibindo o estado inicial do jogo
    #print(f"Mão do jogador {jogador1.nome}: {jogador1.mao}")
    #print(f"Mão do jogador {jogador2.nome}: {jogador2.mao}")
#print(f"\nPrimeira carta aberta na mesa: {carta_mesa}")\

jogador_inicial = inicio_turno(jogadores)
indice_jogador = jogadores.index(jogador_inicial)

# Loop principal do jogo
while True:
    jogador_atual = jogadores[indice_jogador]
    print(f"\n--- Turno de {jogador_atual.nome} ---")
    resultado_turno = turno(jogador_atual, baralho, carta_mesa, jogadores, indice_jogador)

    if resultado_turno is not None:
        carta_mesa = resultado_turno

    if not jogador_atual.mao:
        print(f"\n{jogador_atual.nome} venceu o jogo!")
        pontos_partida(jogadores)
        break

    if not baralho:
        print("\nO baralho acabou! O jogo terminou em empate.")
        pontos_partida(jogadores) 
        break
    indice_jogador = (indice_jogador + 1) % len(jogadores)


# Jogador 1 escolhe uma carta válida para jogar
    #carta_jogada_jogador1 = escolher_carta(jogador1, carta_mesa)

    # Jogador 2 escolhe uma carta válida para jogar

    #carta_jogada_jogador2 = escolher_carta(jogador2, carta_jogada_jogador1)

    # Exibindo as mãos e cartas restantes no baralho após as jogadas
print(f"\nMão restante do jogador {jogador1.nome}: {jogador1.mao}")
print(f"Mão restante do jogador {jogador2.nome}: {jogador2.mao}")
print("Cartas restantes no baralho:", len(baralho))

print("\nJogo encerrado.")
print(f"Mão final do jogador {jogador1.nome}: {jogador1.mao}")
print(f"Mão final do jogador {jogador2.nome}: {jogador2.mao}")
print("Cartas restantes no baralho:", len(baralho))



