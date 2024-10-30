'''
Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
'''

valor_a_str = input()
valor_b_str = input()
valor_c_str = input()
valor_d_str = input()

valor_a_int = int(valor_a_str)
valor_b_int = int(valor_b_str)
valor_c_int = int(valor_c_str)
valor_d_int = int(valor_d_str)

diferenca = ((valor_a_int * valor_b_int) - (valor_c_int * valor_d_int))
print(f'DIFERENCA = {diferenca}')