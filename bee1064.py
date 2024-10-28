'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. 
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''
count=0
somatorio=0.0
for i in range(1,7):
    n = float(input())
    if(n>0):
        somatorio = somatorio + n
        count=count+1
print("{} valores positivos".format(count))
print("%0.1f"%(somatorio/count))