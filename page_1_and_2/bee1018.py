'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, 
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, 
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
valor = int(input())

valor_lido = valor

# Variaveis
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

while valor > 0 and valor < 1000000:
    if valor >= 100:
        valor -= 100
        nota_100 += 1
    elif valor >= 50 and valor < 100:
        valor -= 50
        nota_50 += 1
    elif valor >= 20 and valor < 50:
        valor -= 20
        nota_20 += 1
    elif valor >= 10 and valor < 20:
        valor -= 10
        nota_10 += 1
    elif valor >= 5 and valor < 10:
        valor -= 5
        nota_5 += 1
    elif valor >= 2 and valor < 5:
        valor -= 2
        nota_2 += 1
    elif valor >= 1 and valor < 2:
        valor -= 1
        nota_1 += 1

print(valor_lido)
print(f'{nota_100} nota(s) de R$ 100,00')
print(f'{nota_50} nota(s) de R$ 50,00')
print(f'{nota_20} nota(s) de R$ 20,00')
print(f'{nota_10} nota(s) de R$ 10,00')
print(f'{nota_5} nota(s) de R$ 5,00')
print(f'{nota_2} nota(s) de R$ 2,00')
print(f'{nota_1} nota(s) de R$ 1,00')