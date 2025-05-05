'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
Entrada

A entrada contém um valor inteiro N (0 < N < 13).
Saída

A saída contém um valor inteiro, correspondente ao fatorial de N.
'''
fatorial = 0
count = 0

n = int(input())

for i in range(1,n+1):
    if count == 0:
        fatorial = n
        count += 1
    else:
        fatorial = (n-count) * fatorial
        count += 1
    
print(fatorial)