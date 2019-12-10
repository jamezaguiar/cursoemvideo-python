#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual é o salário do funcionário?: R$"))
aumento = salario*15/100
print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}".format(salario,salario+aumento))