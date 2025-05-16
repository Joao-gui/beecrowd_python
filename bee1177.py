'''
Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.

Entrada
A entrada contém um valor inteiro T (2 ≤ T ≤ 50).

Saída
Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
'''
t = int(input())
count = 0
xList = []

while count < 1000:
    for j in range(t):
        xList.append(j)
        print(f'N[{count}] = {xList[count]}')
        count += 1
        if count == 1000:
            break