'''
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, 
pois pode ser dividido apenas pelo número 1 e pelo número 7.
Entrada

A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), 
indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
Saída

Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.
'''
testCases = int(input())
count = 0

while count < testCases:
    number = int(input())

    count2 = 2
    isNumberPrime = True

    while count2 < number:
        if number % count2 != 0:
            count2 += 1
        else:
            isNumberPrime = False
            break

    if isNumberPrime == True:
        print(f'{number} eh primo')

    elif isNumberPrime == False:
        print(f'{number} nao eh primo')

    count += 1