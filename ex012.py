# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. #

preco = float(input('Qual é o preço do produto? R$'))
# se o desconto é de 5%, então é 95%*preço #
precoDesc = 0.95*preco
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, precoDesc))
