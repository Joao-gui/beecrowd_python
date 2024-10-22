'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
def calculo_horas(hora_inicial, hora_final):
    if hora_inicial < hora_final:
        duracao = hora_final - hora_inicial
        return duracao
    else:
        duracao = (24 - hora_inicial) + hora_final
        return duracao

def calculo_minutos(minuto_inicial, minuto_final):
    if minuto_inicial < minuto_final:
        duracao = minuto_final - minuto_inicial
        return duracao
    elif minuto_inicial == minuto_final:
        return 0
    else:
        duracao = 60 - (minuto_inicial - minuto_final)
        return duracao

hora_i, minuto_i, hora_f, minuto_f = map(int, input().split())
retorno_horas = calculo_horas(hora_i, hora_f)
retorno_minutos = calculo_minutos(minuto_i, minuto_f)
print(f'O JOGO DUROU {retorno_horas} HORA(S) E {retorno_minutos} MINUTO(S)')

# Corrigir erro quando da 59 minutos e aparece 1H, entrada exemplo 7 10 8 9