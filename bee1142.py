'''
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
'''
lista_numeros = []
j = 1
x = int(input())

for i in range(x):
    for j in range(j, j+3):
        lista_numeros.append(j)
    print(*lista_numeros, sep=' ', end= ' ')
    print('PUM')
    lista_numeros = []
    j += 2