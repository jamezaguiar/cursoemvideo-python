# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print("========== LOJAS GUANABARA ==========")

preco = float(input("Preço das compras: R$"))

print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input("Qual é a opção? "))

if (opcao == 1):
    precoFinal = preco - ((10/100)*preco)

elif (opcao == 2):
    precoFinal = preco - ((5/100)*preco)

elif (opcao == 3):
    precoFinal = preco

elif (opcao == 4):
    precoFinal = preco + ((20/100)*preco)
    qtdParcelas = int(input("Quantas parcelas? "))
    valorParcelas = precoFinal/qtdParcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(
        qtdParcelas, valorParcelas))

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(
    preco, precoFinal))
