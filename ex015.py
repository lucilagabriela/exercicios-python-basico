# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. #

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
# dado que o carro custa R$60 por dia e R$0.15 por km rodado #
precoDias = 60*dias
precoKm = 0.15*km
totalPreco = precoDias + precoKm
print('O total a pagar por {} dias e {}km rodados é de R${}'.format(dias, km, totalPreco))