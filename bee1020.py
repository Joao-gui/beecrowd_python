'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''
valor_entrada = int(input())

valor_anos = 0
valor_meses = 0
valor_dias = 0

while valor_entrada > 0:
    if valor_entrada >= 365:
        valor_anos += 1
        valor_entrada -= 365

    elif valor_entrada >= 30:
        valor_meses += 1
        valor_entrada -= 30

    else:
        valor_dias = valor_entrada
        valor_entrada = 0

print(f'{valor_anos} ano(s)')
print(f'{valor_meses} mes(es)')
print(f'{valor_dias} dia(s)')