'''
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. 
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. 
Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. 
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número 
de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. 
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. 
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
'''
cont_grenal = 0
gols_inter = 0
gols_gremio = 0
empates = 0
while True:
    x ,y = map(int, input().split())
    t = 0
    cont_grenal += 1
    if x > y:
        gols_inter += 1
    elif x < y:
        gols_gremio += 1
    else:
        empates += 1
    while True:
        print('Novo grenal (1-sim 2-nao)')
        t = int(input())
        if (t == 1 or t == 2):
            break
    if (t == 2):
        print(f'{cont_grenal} grenais')
        print(f'Inter:{gols_inter}')
        print(f'Gremio:{gols_gremio}')
        print(f'Empates:{empates}')
        if gols_inter > gols_gremio:
            print('Inter venceu mais')
        elif gols_gremio > gols_inter:
            print('Gremio venceu mais')
        elif gols_gremio == gols_inter:
            print('Nao houve vencedor')
        break