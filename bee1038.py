'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. 
A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''
valor_codigo, valor_qnt = map(float, input().split())

total = 0

if valor_codigo == 1:
    total = valor_qnt * 4

elif valor_codigo == 2:
    total = valor_qnt * 4.5

elif valor_codigo == 3:
    total = valor_qnt * 5.0

elif valor_codigo == 4:
    total = valor_qnt * 2

elif valor_codigo == 5:
    total = valor_qnt * 1.5

print(f'Total: R$ {total:.2f}')