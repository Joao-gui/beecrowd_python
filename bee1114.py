'''
Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" 
e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.
'''
senha_correta = 2002
cond = 0

while(cond == 0):
    senha_digitada = int(input())
    if senha_digitada == senha_correta:
        print('Acesso Permitido')
        cond = 1
    else:
        print('Senha Invalida')