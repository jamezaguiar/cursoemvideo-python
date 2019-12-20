# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
jogadaComputador = randint(0, 2)

print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

jogadaUsuario = int(input("Qual é a sua jogada? "))

if (jogadaComputador == 0 and jogadaUsuario == 0):
    print("Computador jogou Pedra\nJogador jogou Pedra")
    print("EMPATE!")
elif (jogadaComputador == 0 and jogadaUsuario == 1):
    print("Computador jogou Pedra\nJogador jogou Papel")
    print("JOGADOR VENCE")
elif (jogadaComputador == 0 and jogadaUsuario == 2):
    print("Computador jogou Pedra\nJogador jogou Tesoura")
    print("COMPUTADOR VENCE")
elif (jogadaComputador == 1 and jogadaUsuario == 0):
    print("Computador jogou Papel\nJogador jogou Pedra")
    print("COMPUTADOR VENCE")
elif (jogadaComputador == 1 and jogadaUsuario == 1):
    print("Computador jogou Papel\nJogador jogou Papel")
    print("EMPATE!")
elif (jogadaComputador == 1 and jogadaUsuario == 2):
    print("Computador jogou Papel\nJogador jogou Tesoura")
    print("JOGADOR VENCE")
elif (jogadaComputador == 2 and jogadaUsuario == 0):
    print("Computador jogou Tesoura\nJogador jogou Pedra")
    print("JOGADOR VENCE")
elif (jogadaComputador == 2 and jogadaUsuario == 1):
    print("Computador jogou Tesoura\nJogador jogou Papel")
    print("COMPUTADOR VENCE")
elif (jogadaComputador == 2 and jogadaUsuario == 2):
    print("Computador jogou Tesoura\nJogador jogou Tesoura")
    print("EMPATE!")
elif (jogadaUsuario > 2 or jogadaUsuario < 0):
    print("Opção inválida")
    print("COMPUTADOR VENCE")
