'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura. (A=bh/2)
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, 
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. 
O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
'''
valor_A_float, valor_B_float, valor_C_float = map(float, input().split())
# valor_B_str = input()
# valor_C_str = input()

# valor_A_float = float(valor_A_str)
# valor_B_float = float(valor_B_str)
# valor_C_float = float(valor_C_str)

pi = 3.14159

area_triangulo = (valor_A_float * valor_C_float) / 2
area_circulo = pi * pow(valor_C_float, 2)
area_trapezio = (valor_A_float + valor_B_float) * valor_C_float / 2
area_quadrado = pow(valor_B_float, 2)

area_retangulo = valor_A_float * valor_B_float
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')