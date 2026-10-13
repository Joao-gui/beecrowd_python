'''
Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) 
é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. 
Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20), 
indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com a especificação fornecida.
'''
testCases = int(input())
count = 0

while count < testCases:
    number = int(input())

    count2 = 1
    numberSum = 0

    while count2 < number:
        if number % count2 == 0:
            numberSum += count2
            count2 += 1
        else:
            count2 += 1

    if numberSum == number:
        print(f'{number} eh perfeito')

    else:
        print(f'{number} nao eh perfeito')

    count += 1