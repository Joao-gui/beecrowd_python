'''
Faça um programa que leia 6 valores. 
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''
numeros = range(6)
i = 0
count = 0
for i in numeros:
    numero_str = input()
    numero_float = float(numero_str)

    if numero_float > 0:
        count += 1

print(f'{count} valores positivos')