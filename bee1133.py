'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre 
eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.
'''
def calculoMaiorMenor(x,y):
    if x > y:
        maior = x
        menor = y
        return(maior,menor)
    elif y > x:
        maior = y
        menor = x
        return(maior,menor)

x = int(input())
y = int(input())

maior, menor = calculoMaiorMenor(x, y)

for i in range(menor+1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)