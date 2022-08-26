# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# para inferiores ou iguais a 1.250, o aumento é de 15%
salario = float(input('Digite seu salário para saber seu aumento: '))
if salario > 1250:
    novoSal = 1.10*salario
    desconto = 10
else:
    novoSal = 1.15*salario
    desconto = 15
print('Com um salário de R${}, seu novo salário é de R${}, com aumento de {}%.'.format(salario, novoSal, desconto))