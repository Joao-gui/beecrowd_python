'''
Você deve fazer um programa que leia um valor qualquer e 
apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.
'''
valor_entrada = float(input())

if valor_entrada >= 0 and valor_entrada <= 25:
    print('Intervalo [0,25]')
elif valor_entrada > 25 and valor_entrada <= 50:
    print('Intervalo (25,50]')
elif valor_entrada > 50 and valor_entrada <= 75:
    print('Intervalo (50,75]')
elif valor_entrada > 75 and valor_entrada <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')