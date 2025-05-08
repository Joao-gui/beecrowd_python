'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.
'''
n = int(input())
count = 0

# Condição de repetição par aquantidade de fezes a digitar
while count < n:
    x, y = map(int,input().split())
    soma = 0    
    count_impar = 0

    # Teste para saber se o primeiro numero é par
    if x % 2 == 0:
        x += 1

    # Loop para soma de impares
    while count_impar < y:
        soma += x
        count_impar += 1
        # Condição para sempre o próximo número X for ímpar.
        x += 2

    print(soma)
    count += 1

