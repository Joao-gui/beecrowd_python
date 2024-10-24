'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, 
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, 
sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. 
Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

Tabela no site.

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, 
pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. 
No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, 
o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, 
com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".
'''
def calculo(salario):
    if salario <= 2000:
        return 0        
    elif salario > 2000 and salario <= 3000:
        novo_valor = salario - 2000
        valor_imposto = novo_valor * 0.08
        return valor_imposto
    elif salario > 3000 and salario <= 4500:
        novo_valor = 1000 * 0.08
        novo_valor2 = salario - 3000
        valor_imposto = (novo_valor2 * 0.18) + novo_valor
        return valor_imposto
    elif salario > 4500:
        novo_valor = 1000 * 0.08
        novo_valor2 = 1500 * 0.18
        novo_valor3 = salario - 4500
        valor_imposto = (novo_valor3 * 0.28) + novo_valor2 + novo_valor
        return valor_imposto

salario_str = input()
salario_float = float(salario_str)
calculo_return = calculo(salario_float)

if calculo_return == 0:
    print('Isento')
else:
    print(f'R$ {calculo_return:.2f}')