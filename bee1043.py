'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''
def calcular_perimetro_area(lado_a, lado_b, lado_c):
    lado_ab = lado_a + lado_b
    lado_ac = lado_a + lado_c
    lado_bc = lado_b + lado_c

    if lado_a < lado_bc:
        if lado_b < lado_ac:
            if lado_c < lado_ab:
                perimetro = float(lado_a + lado_b + lado_c)
                print(f'Perimetro = {perimetro:.1f}')
            else:
                area = float((lado_a + lado_b) * lado_c) / 2
                print(f'Area = {area:.1f}')
        else:
            area = float((lado_a + lado_b) * lado_c) / 2
            print(f'Area = {area:.1f}')
    else:
        area = float((lado_a + lado_b) * lado_c) / 2
        print(f'Area = {area:.1f}')

lado_a, lado_b, lado_c = map(float, input().split())
calcular_perimetro_area(lado_a, lado_b, lado_c)