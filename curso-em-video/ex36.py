# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anosPagamento = float(input('Por quantos anos irá pagar? '))
prestacaoMensal = valorCasa/(anosPagamento*12)
if prestacaoMensal > 0.3*salario:
    print('EMPRÉSTIMO NEGADO! A prestação seria de R${:.3f} e ficou muito alta!'.format(prestacaoMensal))
else:
    print('EMPRÉSTIMO CONCEDIDO! Sua prestação mensal será de R${:.2f}.'.format(prestacaoMensal))