# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# R$0.50 por km, em até 200km; R$0.45 para mais longas
distancia = float(input('Qual a distância da viagem, em km: '))
if distancia <= 200:
    precoPassagem = 0.50*distancia
else:
    precoPassagem = 0.45*distancia
print('Você terá que pagar R${:.2f} pela sua viagem de {}km.'.format(precoPassagem, distancia))