'''
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
'''

media_idades = 0
soma_idades = 0
idade_lista = []
count = 0

idades = int(input())

while idades >= 0:
    count += 1
    idade_lista.append(idades)
    idades = int(input())

for i in idade_lista:
    soma_idades += i

media_idades = soma_idades / count
print(f"{media_idades:.2f}")