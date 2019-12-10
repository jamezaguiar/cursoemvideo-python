#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input("Digite um número para ver sua tabuada de multiplicação: "))
print("---------------")
i = 1
while(i<=10):
    print("{} x {} = {}".format(num,i,(num*i)))
    i+=1
print("---------------")