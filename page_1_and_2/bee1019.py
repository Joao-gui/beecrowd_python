'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
valor_entrada = int(input())

valor_h = 0
valor_min = 0
valor_seg = 0

while valor_entrada > 0:
    if valor_entrada >= 3600:
        valor_h += 1
        valor_entrada -= 3600

    elif valor_entrada >= 60:
        valor_min += 1
        valor_entrada -= 60

    elif valor_entrada >= 1:
        valor_seg += 1
        valor_entrada -= 1

print(f'{valor_h}:{valor_min}:{valor_seg}')