'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, 
de modo que o lado A representa o maior dos 3 lados. A seguir, 
determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''
import math

def trigangulos(lista):
    lado_x_list = lista[0]
    lado_x = float(lado_x_list)
    lado_y_list = lista[1]
    lado_y = float(lado_y_list)
    lado_z_lista = lista[2]
    lado_z = float(lado_z_lista)

    if lado_x >= (lado_y + lado_z):
        print('NAO FORMA TRIANGULO')

    else:
        if math.pow(lado_x,2) == (math.pow(lado_y,2) + math.pow(lado_z,2)):
            print('TRIANGULO RETANGULO')

        if math.pow(lado_x,2) > (math.pow(lado_y,2) + math.pow(lado_z,2)):
            print('TRIANGULO OBTUSANGULO')

        if math.pow(lado_x,2) < (math.pow(lado_y,2) + math.pow(lado_z,2)):
            print('TRIANGULO ACUTANGULO')

        if lado_x == lado_y and lado_x == lado_z:
            print('TRIANGULO EQUILATERO')

        elif lado_x == lado_y or lado_x == lado_z or lado_y == lado_z:
            print('TRIANGULO ISOSCELES')

def lista(lado_a, lado_b, lado_c):
    lista_inicial = [lado_a, lado_b, lado_c]
    lista_dec = (sorted(lista_inicial, reverse=True))
    return trigangulos(lista_dec)

lado_a, lado_b, lado_c = map(float, input().split())
lista(lado_a, lado_b, lado_c)