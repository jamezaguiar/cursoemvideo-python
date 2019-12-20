# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
primeiroSegmento = float(input("Primeiro segmento: "))
segundoSegmento = float(input("Segundo segmento: "))
terceiroSegmento = float(input("Terceiro segmento: "))

if primeiroSegmento < segundoSegmento + terceiroSegmento and segundoSegmento < primeiroSegmento + terceiroSegmento and terceiroSegmento < primeiroSegmento + segundoSegmento:
    print("Os segmentos acima PODEM FORMAR triângulo", end=' ')
    if (primeiroSegmento == segundoSegmento and primeiroSegmento == terceiroSegmento and segundoSegmento == terceiroSegmento):
        print("EQUILÁTERO")
    elif ((primeiroSegmento == segundoSegmento and primeiroSegmento != terceiroSegmento) or (primeiroSegmento == terceiroSegmento and primeiroSegmento != segundoSegmento) or (segundoSegmento == terceiroSegmento and segundoSegmento != primeiroSegmento)):
        print("ISÓSCELES")
    elif ((primeiroSegmento != segundoSegmento and primeiroSegmento != terceiroSegmento and segundoSegmento != terceiroSegmento)):
        print("ESCALENO")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")
