'''
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. 
Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, 
você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. 
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, 
imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.
'''
pares = []
impares = []
cont = 0

#Função printar vetor
def meuVetor(minhaString, vetor):
    for index, valor in enumerate(vetor):
        print(f'{minhaString}[{index}] = {valor}')

while cont < 15:
    valor = int(input())
    #Verificando se é par
    if valor % 2 == 0:
        pares.append(valor)
        #Verificando tamanho do vetor
        if len(pares) == 5:
            meuVetor('par', pares)
            pares.clear()
    #Se não for par é impar
    else:
        impares.append(valor)
        #Verificando tamanho do vetor
        if len(impares) == 5:
            meuVetor('impar', impares)
            impares.clear()
    cont += 1

#Printando o resto dos numeros de cada vetor
#Verificando tamanho do vetor
meuVetor('impar', impares)
meuVetor('par', pares)