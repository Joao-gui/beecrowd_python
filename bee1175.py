'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
'''
xList = []

for i in range(20):    
    valor = int(input())
    xList.append(valor)
pos = 0

for l in xList[::-1]:
    print(f"N[{pos}] = {l}")
    pos += 1