# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1+nota2)/2
print("Tirando {:.2f} e {:.2f} a média do aluno é {:.2f}".format(
    nota1, nota2, media))
if (media < 5.0):
    print("O aluno está REPROVADO.")
elif (media < 7.0):
    print("O aluno está de RECUPERAÇÂO.")
else:  # Se os dois casos acima são falsos, isso significa que a média é maior que 7
    print("O aluno está APROVADO.")
