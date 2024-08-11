'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, 
portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
valor_A, valor_B, valor_C = map(int, input().split())

maior = (valor_A + valor_B + abs(valor_A - valor_B)) / 2

maior = int(maior)

if valor_C > maior:
    print(f'{valor_C} eh o maior')

else:
    print(f'{maior} eh o maior')