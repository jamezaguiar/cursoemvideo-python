#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo,cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo,tangente))

#As funções de seno, cosseno e tangente do python recebem como parâmetro um número em radianos