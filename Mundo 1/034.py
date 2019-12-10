#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual é o salário do funcionário?: R$"))
if salario >=1250.00:
    novosalario = salario+((10*salario)/100)
    print("O novo salário será R${:.2f}!".format(novosalario))
else:
    novosalario = salario+((15*salario)/100)
    print("O novo salário será R${:.2f}!".format(novosalario))