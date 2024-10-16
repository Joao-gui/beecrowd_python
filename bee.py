#x = input()
#x1 = float(x)
#
#produto = {'Codigo': 1,
#           'Produto': 'Arroz',
#           'Preco': 2.0,
#        }
#
## print(produto['Codigo'])
#
#for item in produto:
#    print(item, produto[item])
#
#print(x)
#
#nova_lista = {**produto,
#              'Codigo': produto['Codigo'] + x1,
#              #'Produto': produto['Produto'],
#              'Preco': produto['Preco'] * x1,
#        }
#
#for item2 in nova_lista:
#    print(item2, nova_lista[item2])

# ----------------
x, y = map(float, input().split())
x1 = float(x)
y1 = int(y)

produto = [
    {   
        'Codigo': 1,
        'Produto': 'Arroz',
        'Preco': 2.0,
    },
    {
        'Codigo': 2,
        'Produto': 'Feijão',
        'Preco': 4.0,
    },
]
#print(produto[1])
#print()

for item in produto:
    for item2 in item:
        print(item2, item[item2])
    #print(item)
    print()

nova_lista = [
    {**item, 'Preco': item['Preco'] * x1}
    for item in produto
]

for item in nova_lista:
    for item2 in item:
        print(item2, item[item2])
    #print(item)
    print()