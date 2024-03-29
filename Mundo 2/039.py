# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
dataAtual = date.today()
anoAtual = dataAtual.year

nasc = int(input("Ano de nascimento: "))
idade = anoAtual-nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, anoAtual))
if (idade < 18):
    print("Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.".format(
        18-idade, nasc+18))
elif (idade > 18):
    print("Você já deveria ter se alistado a {} anos.\nSeu alistamento foi em {}.".format(
        idade-18, nasc+18))
elif (idade == 18):
    print("Você tem que se alistar IMEDIATAMENTE!")
