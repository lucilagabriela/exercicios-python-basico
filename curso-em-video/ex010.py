reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = reais/5.11
euro = reais/5.10
iene = reais/0.037
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f} e ¥{:.2f}'.format(reais, dolar, euro, iene))