'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", 
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
'''
def multiplo (numero_a, numero_b):
    if numero_a > numero_b:
        resultado = numero_a % numero_b

    elif numero_a < numero_b:
        resultado = numero_b % numero_a

    if resultado == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

numero_a, numero_b = map(int, input().split())
multiplo(numero_a, numero_b)