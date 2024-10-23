'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

Percentual de Reajuste
15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) 
e o percentual de reajuste ganho, conforme exemplo abaixo.
'''
def calculo_salario(salario):
    if salario <= 400:
        reajuste_ganho = salario * 0.15
        novo_salario = salario + reajuste_ganho
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste_ganho:.2f}')
        print('Em percentual: 15 %')

    elif salario >= 400.01 and salario <= 800:
        reajuste_ganho = salario * 0.12
        novo_salario = salario + reajuste_ganho
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste_ganho:.2f}')
        print('Em percentual: 12 %')

    elif salario >= 800.01 and salario <= 1200:
        reajuste_ganho = salario * 0.10
        novo_salario = salario + reajuste_ganho
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste_ganho:.2f}')
        print('Em percentual: 10 %')

    elif salario >= 1200.01 and salario <= 2000:
        reajuste_ganho = salario * 0.07
        novo_salario = salario + reajuste_ganho
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste_ganho:.2f}')
        print('Em percentual: 7 %')

    elif salario > 2000:
        reajuste_ganho = salario * 0.04
        novo_salario = salario + reajuste_ganho
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste_ganho:.2f}')
        print('Em percentual: 4 %')

salario = float(input())
calculo_salario(salario)