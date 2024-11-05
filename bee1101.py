'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
'''
n, m = map(int, input().split())
soma = 0
lsita_numeros = []

while(n > 0 and m > 0):
    if n > m:
        for m in range(m, n+1):
            soma += m
            lsita_numeros.append(m)
            m += 1
        #print(' '.join(map(str, lsita_numeros)) + f' Sum={soma}')
        print(*lsita_numeros, sep=' ', end= ' ')
        print(f'Sum={soma}')
    elif n < m:
        for n in range(n, m+1):
            soma += n
            lsita_numeros.append(n)
            n += 1
        #print(' '.join(map(str, lsita_numeros)) + f' Sum={soma}')
        print(*lsita_numeros, sep=' ', end= ' ')
        print(f'Sum={soma}')
    else:
        print(f'{n} Sum={n}')
    lsita_numeros = []
    soma = 0
    n, m = map(int, input().split())