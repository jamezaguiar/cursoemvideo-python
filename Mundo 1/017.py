#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
print("A hipotenusa vai medir {:.2f}".format(hypot(oposto,adjacente)))

#O cálculo é: (oposto**2 + adjacente**2) ** (1/2)