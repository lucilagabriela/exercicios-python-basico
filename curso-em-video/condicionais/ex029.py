# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# considerando que a multa custa R$7 por cada km acima do limite
velInicial = float(input('Qual a velocidade atual? '))
if velInicial <=80:
    print('Parabéns, você não foi multado!')
else:
    multa = (velInicial-80)*7
    print('Você foi multado, pois atingiu {:.2f}km/h. Terá de pagar R${} em multa!'.format(velInicial, multa))