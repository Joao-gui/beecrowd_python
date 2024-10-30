'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, 
da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Gráfico no site.

Entrada
A entrada contém 3 palavras, uma em cada linha, 
necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''
def fluxo(subfilo, subclasse, animais):
    if subfilo == 'vertebrado':
        if subclasse == 'ave':
            if animais == 'carnivoro':
                print('aguia')
            elif animais == 'onivoro':
                print('pomba')
        elif subclasse == 'mamifero':
            if animais == 'onivoro':
                print('homem')
            elif animais == 'herbivoro':
                print('vaca')
    elif subfilo == 'invertebrado':
        if subclasse == 'inseto':
            if animais == 'hematofago':
                print('pulga')
            elif animais == 'herbivoro':
                print('lagarta')
        elif subclasse == 'anelideo':
            if animais == 'hematofago':
                print('sanguessuga')
            elif animais == 'onivoro':
                print('minhoca')

opcao1 = input()
opcao2 = input() 
opcao3 = input()
fluxo_return = fluxo(opcao1, opcao2, opcao3)