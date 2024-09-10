'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. 
Imprima sempre o final de linha após cada mensagem.
'''
import math

valor_A, valor_B, valor_C = map(float, input().split())

valor_x1 = 0
valor_x2 = 0
valor_delta = 0

if valor_A > 0:
    valor_delta = pow(valor_B, 2) - (4 * valor_A * valor_C)

    if valor_delta >= 0:
        valor_x1 = (-1 * valor_B + math.sqrt(valor_delta)) / (2 * valor_A)
        valor_x2 = (-1 * valor_B - math.sqrt(valor_delta)) / (2 * valor_A)

        print(f'R1 = {valor_x1:.5f}')
        print(f'R2 = {valor_x2:.5f}')
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')