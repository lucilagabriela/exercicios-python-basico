# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
# randint é para números inteiros entre um intervalo dado
nmrComp = random.randint(0, 6) # o valor inferior é incluído, mas o superior não

print('-=-' * 15 + '\nVou pensar em um número entre 0 e 5.\nTente adivinhar...\n'+'-=-' * 15)
nmrUsuario = int(input('Em que número eu pensei? '))
print('Calma...')
time.sleep(2)
if nmrUsuario == nmrComp:
    print('Você acertou!! O número que eu pensei foi {}.'.format(nmrComp))
else:
    print('Que pena. Você errou! O número que eu pensei foi {}.'.format(nmrComp))
