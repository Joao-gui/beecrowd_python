'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
j = 0
posicao = 0
for i in range(100):
    n  = int(input())
    if(n>j):
        j = n
        posicao = i
print(j)
print(posicao + 1)