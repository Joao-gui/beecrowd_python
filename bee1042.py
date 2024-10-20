'''
Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''
valor_a, valor_b, valor_c = map(int, input().split())

valor_inicial = [valor_a, valor_b, valor_c]
valor_crescente = sorted(numero for numero in valor_inicial)

# print(valor_inicial)
# print(valor_crescente)

# Trsnforma Lista em linhas
for nuemeros_crescente in valor_crescente:
    print(nuemeros_crescente)

print()

for numeros_inicial in valor_inicial:
    print(numeros_inicial)