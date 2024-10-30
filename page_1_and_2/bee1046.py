'''
Leia a hora inicial e a hora final de um jogo. 
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, 
tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''
def calculo_horas(hora_inicial, hora_final):
    if hora_inicial < hora_final:
        duracao = hora_final - hora_inicial
        return duracao
    else:
        duracao = (24 - hora_inicial) + hora_final
        return duracao

hora_inicial, hora_final = map(int, input().split())
duracao_1 = calculo_horas(hora_inicial, hora_final)
print(f'O JOGO DUROU {duracao_1} HORA(S)')