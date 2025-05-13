'''
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
'''
j = 0
number = 0
xList = []
for i in range(10):
    number = int(input())
    xList.append(number)

for numberList in xList:
    if numberList <= 0:
        numberList = 1    
    print(f'X[{j}] = {numberList}')
    j += 1