#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input("Uma distância em metros: "))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print("A medida de {}m corresponde a".format(metros))
print("{}km".format(km))
print("{}hm".format(hm))
print("{}dam".format(dam))
print("{}dm".format(dm))
print("{}cm".format(cm))
print("{}mm".format(mm))