# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

def porcentagem (num, porcent):
    resultado = num * porcent / 100
    return resultado

valorCasa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?: "))
qtdPrestacoes = 12 * anos
valorPrestacoes = valorCasa / qtdPrestacoes
porcentagemSalario = porcentagem(salario, 30)

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(valorCasa,anos,valorPrestacoes))

if (valorPrestacoes > porcentagemSalario):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")