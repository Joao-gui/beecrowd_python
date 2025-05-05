'''
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. 
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 46).
Saída

Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.
'''
n = int(input())
n_ultimo = 1
n_penultimo = 0
lista_fibo = []
count = 0

while count < n:
    if count < 2:
        lista_fibo.append(str(count))
        count += 1
    else:
        termo = n_ultimo + n_penultimo
        n_penultimo = n_ultimo
        n_ultimo = termo
        count += 1
        lista_fibo.append(str(termo))

numeros = " ".join(lista_fibo)
print(numeros)