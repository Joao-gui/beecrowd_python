'''
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. 
A seguir mostre a variável PROD com mensagem correspondente.   

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. 
Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
variavel_a_str = input()
variavel_b_str = input()
variavel_a_int = int(variavel_a_str)
variavel_b_int = int(variavel_b_str)
prod = variavel_a_int * variavel_b_int
print(f'PROD = {prod}')