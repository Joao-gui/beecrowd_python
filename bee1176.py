'''
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. 
Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. 
Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), 
correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
'''
t = int(input())
count = 0

for count in range(t):
    fNumber = int(input())
    x1Number = 0
    x2Number = 1
    j = 0

    if fNumber == 0:
        print(f'Fib({fNumber}) = {x1Number}')

    elif fNumber == 1:
        print(f'Fib({fNumber}) = {x2Number}')

    else:    
        for j in range(2,fNumber + 1):
            x3Number = x1Number + x2Number
            x1Number = x2Number
            x2Number = x3Number
            j += 1
        print(f'Fib({fNumber}) = {x3Number}')