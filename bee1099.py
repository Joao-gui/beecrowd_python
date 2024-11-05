'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''
n = int(input())
i = 0
j = 0
soma_impar = 0

for i in range(n):
    valorX, valorY = map(int, input().split())
    dif = abs(valorX - valorY)

    if valorX > valorY:
        for j in range(1, dif):
            valorY += 1
            if valorY % 2 != 0:
                soma_impar += valorY
    elif valorX < valorY:
        for j in range(1, dif):
            valorX += 1
            if valorX % 2 != 0:
                soma_impar += valorX
    print(soma_impar)
    soma_impar = 0