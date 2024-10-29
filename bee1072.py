'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
'''
n = int(input())
n_in = 0
n_out = 0

if n < 10000:
    for i in range(n):
        x = int(input())
        if x >= 10 and 20 >= x:
            n_in += 1
        else:
            n_out += 1

print(f'{n_in} in')
print(f'{n_out} out')