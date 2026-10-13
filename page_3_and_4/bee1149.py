'''
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). 
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
'''
a = 0
n = 0
soma = 0

entrada = input()
numeros = list(map(int, entrada.split()))

for item in numeros:
    if item > 0:
        if a == 0:
            a = item
        else:
            n = item
    else:
        pass

for i in range(n):
    soma = i + a + soma

print(soma)