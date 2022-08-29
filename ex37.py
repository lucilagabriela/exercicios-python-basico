# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

nmr = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n')
conversao = int(input('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\n'))
if conversao == 1:
    novoNmr = bin(nmr)
    print(novoNmr)
elif conversao == 2:
    novoNmr = oct(nmr)
    print(novoNmr)
elif conversao == 3:
    novoNmr = hex(nmr)
    print(novoNmr)
else:
    print('ERRO! Será que você digitou errado?')