'''
Leia um valor inteiro entre 1 e 12, inclusive. 
Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
'''
mes_str = input()
mes_int = int(mes_str)

match mes_int:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June')
    case 7:
        print('July')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('October')
    case 11:
        print('November')
    case 12:
        print('December')
    case _:
        exit