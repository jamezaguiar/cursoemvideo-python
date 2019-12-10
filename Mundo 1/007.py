#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
notaum = float(input("Digite a primeira nota: "))
notadois = float(input("Digite a segunda nota: "))
media = (notaum+notadois)/2
print ("A média entre {} e {} é igual a {:.2f}".format(notaum,notadois,media))