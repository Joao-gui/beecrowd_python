'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e 
precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, 
o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a 
quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o 
percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
N=int(input())
cont,rato,sapo,coelho=0,0,0,0
for i in range(N):
    Quantia,Tipo=input().split()
    str(Tipo)
    cont+=int(Quantia)
    if Tipo== 'C':
        coelho +=int(Quantia)
    elif Tipo=='R':
        rato+=int(Quantia)
    elif Tipo=='S':
        sapo+=int(Quantia)

print('Total: %d cobaias' %cont)
print('Total de coelhos: %d' %coelho)
print('Total de ratos: %d' %rato)
print('Total de sapos: %d' %sapo)
print('Percentual de coelhos: %.2f' %float(((100*coelho)/cont)),'%')
print('Percentual de ratos: %.2f' %float(((100*rato)/cont)),'%')
print('Percentual de sapos: %.2f' %float(((100*sapo)/cont)),'%')