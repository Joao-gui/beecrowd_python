'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, 
com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. 
Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
'''

# This Python code snippet is reading three input values from the user, which are the grades of a
# student (A, B, and C). The grades are initially read as strings using the `input()` function and
# then converted to floating-point numbers using the `float()` function.
nota_a_str = input()
nota_b_str = input()
nota_c_str = input()

nota_a_float = float(nota_a_str)
nota_b_float = float(nota_b_str)
nota_c_float = float(nota_c_str)

media = ((nota_a_float * 2) + (nota_b_float * 3) + (nota_c_float * 5)) / 10
print(f'MEDIA = {media:.1f}')