'''
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, 
e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável 
A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
'''
valor_A, valor_B, valor_C, valor_D = map(int, input().split())

if valor_B > valor_C and valor_D > valor_A:
    if (valor_C + valor_D) > (valor_A + valor_B):
        if valor_C > 0 and valor_D > 0:
            if valor_A % 2 == 0:
                print('Valores aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')