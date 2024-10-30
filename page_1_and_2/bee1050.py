'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. 
Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

Tabela no site.

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. 
Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
'''
opcao_str = input()
opcao_int = int(opcao_str)

match opcao_int:
    case 61:
        print('Brasilia')
    case 71:
        print('Salvador')
    case 11:
        print('Sao Paulo')
    case 21:
        print('Rio de Janeiro')
    case 32:
        print('Juiz de Fora')
    case 19:
        print('Campinas')
    case 27:
        print('Vitoria')
    case 31:
        print('Belo Horizonte')
    case _:
        print('DDD nao cadastrado')