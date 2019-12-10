#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Informe a temperatura em graus °C: "))
fahrenheit = ((celsius/5)*9)+32
print("A temperatura de {}°C corresponde a {:.1f}°F!".format(celsius,fahrenheit))