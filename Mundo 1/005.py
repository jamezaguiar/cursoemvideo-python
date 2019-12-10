#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Digite um número: "))
ant = num-1
suc = num+1
print("Analisando o número %d, seu antecessor é %d e seu sucessor é %d" % (num,ant,suc))
