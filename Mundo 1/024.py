#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
c = str(input("Digite o nome da sua cidade: ")).strip()
cd = c.split() #Divida a string em micro espaços e manda verificar o primeiro espaço
print("SANTO" in cd[0].upper())