'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
def calculo_minutos_horas(hora_inicial, minuto_inicial, hora_final, minuto_final):
    minutos_iniciais = hora_inicial * 60 + minuto_inicial
    minutos_finais = hora_final * 60 + minuto_final
    if minutos_iniciais < minutos_finais:
        duracao = minutos_finais - minutos_iniciais
    else:
        duracao = 24 * 60 - minutos_iniciais + minutos_finais
    horas = duracao // 60
    minutos = duracao % 60
    return horas, minutos

hora_i, minuto_i, hora_f, minuto_f = map(int, input().split())
horas, minutos = calculo_minutos_horas(hora_i, minuto_i, hora_f, minuto_f)
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')