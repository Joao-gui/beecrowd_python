'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
valor_entrada = float(input())

#variáveis
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0

moeda_1 = 0
moeda_50 = 0
moeda_25 = 0
moeda_10 = 0
moeda_05 = 0
moeda_01 = 0

while valor_entrada > 0 and valor_entrada < 1000000:
    if valor_entrada >= 100:
        valor_entrada -= 100
        nota_100 += 1
    elif valor_entrada >= 50 and valor_entrada < 100:
        valor_entrada -= 50
        nota_50 += 1
    elif valor_entrada >= 20 and valor_entrada < 50:
        valor_entrada -= 20
        nota_20 += 1
    elif valor_entrada >= 10 and valor_entrada < 20:
        valor_entrada -= 10
        nota_10 += 1
    elif valor_entrada >= 5 and valor_entrada < 10:
        valor_entrada -= 5
        nota_5 += 1
    elif valor_entrada >= 2 and valor_entrada < 5:
        valor_entrada -= 2
        nota_2 += 1
    elif valor_entrada >= 1 and valor_entrada < 2:
        valor_entrada -= 1
        moeda_1 += 1
    elif valor_entrada >= 0.5 and valor_entrada < 1:
        valor_entrada -= 0.5
        moeda_50 += 1
    elif valor_entrada >= 0.25 and valor_entrada < 0.5:
        valor_entrada -= 0.25
        moeda_25 += 1
    elif valor_entrada >= 0.10 and valor_entrada < 0.25:
        valor_entrada -= 0.10
        moeda_10 += 1
    elif valor_entrada >= 0.05 and valor_entrada < 0.10:
        valor_entrada -= 0.05
        moeda_05 += 1
    else:
        moeda_01 = valor_entrada / 0.01
        valor_entrada = 0
#    elif valor_entrada >= 0.01 and valor_entrada < 0.05:
#        valor_entrada -= 0.01
#        moeda_01 += 1

print('NOTAS:')
print(f'{nota_100} nota(s) de R$ 100.00')
print(f'{nota_50} nota(s) de R$ 50.00')
print(f'{nota_20} nota(s) de R$ 20.00')
print(f'{nota_10} nota(s) de R$ 10.00')
print(f'{nota_5} nota(s) de R$ 5.00')
print(f'{nota_2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda_1} moeda(s) de R$ 1.00')
print(f'{moeda_50} moeda(s) de R$ 0.50')
print(f'{moeda_25} moeda(s) de R$ 0.25')
print(f'{moeda_10} moeda(s) de R$ 0.10')
print(f'{moeda_05} moeda(s) de R$ 0.05')
print(f'{moeda_01:.0f} moeda(s) de R$ 0.01')