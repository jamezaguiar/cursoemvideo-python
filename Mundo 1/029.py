#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
kms = float(input("Qual é a velocidade atual do carro?: "))
if kms > 80.0:
    kmsultrapassados = kms-80
    multa = kmsultrapassados*7.00
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}!".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança!")