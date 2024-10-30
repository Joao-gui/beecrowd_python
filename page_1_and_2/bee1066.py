'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, 
quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''
impar = 0
par = 0
positivo = 0
negativo = 0
count = 0
for i in range(5):
    n = int(input())
    count += 1
    if n > 0:
        positivo += 1
        if abs(n) % 2 == 0:
            par += 1
        elif abs(n) % 2 != 0:
            impar += 1
    elif n < 0:
        negativo += 1
        if abs(n) % 2 == 0:
            par += 1
        elif abs(n) % 2 != 0:
            impar += 1
    else:
        par += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(es)')
print(f'{negativo} valor(es) negativo(es)')