'''
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída 
serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. 
Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

Entrada
O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
Imprima a saída conforme o exemplo fornecido.
'''
n=int(input())
for i in range(1,n+1):
    c = i*i
    d= i*i*i
    print("{} {} {}".format(i,c,d))
    e=c+1
    f=d+1
    print("{} {} {}".format(i,e,f))