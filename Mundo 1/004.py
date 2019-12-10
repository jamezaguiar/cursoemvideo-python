# coding: utf-8
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
string = raw_input("Digite algo: ")
print "O tipo primitivo desse valor é", type(string)
print "Só tem espaços?", string.isspace()
print "É um número?", string.isdigit()
print "É alfabético?", string.isalpha()
print "É alfanumérico?", string.isalnum()
print "Está em maiúsculas?", string.isupper()
print "Está em minúsculas?", string.islower()
print "Está capitalizada?", string.istitle()
