'''
<<<<<<< HEAD
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.


=======
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. 
A seguir, calcule e mostre o valor da conta a pagar.
>>>>>>> 7ff57bd94bfe647217101597c1114d7403f349e6

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''
<<<<<<< HEAD
codigo, quantidade = map(int, input().split())

valor = 0.0

if codigo == 1:
    valor = 4 * quantidade
elif codigo == 2:
    valor = 4.50 * quantidade
elif codigo == 3:
    valor = 5 * quantidade
elif codigo == 4:
    valor = 2 * quantidade
elif codigo == 5:
    valor = 1.5 * quantidade

print(f'Total: R$ {valor:.2f}')
=======
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
>>>>>>> 7ff57bd94bfe647217101597c1114d7403f349e6
