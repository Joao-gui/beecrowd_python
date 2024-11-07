'''
Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
'''
import math

lista_numeros = []
pot = 0
i = 1
j = 1

n = int(input())
if n > 1 and n < 1000:
    for j in range(1, n+1):
        for i in range(1, i+3):
            lista_numeros.append(format(int(math.pow(j, i)), 'd'))
        print(*lista_numeros, sep=' ')
        lista_numeros = []
        i = 1