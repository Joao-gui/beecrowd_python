'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''
i = 1
j = 7

while (i <= 9):
    for k in range(3):
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j += 5