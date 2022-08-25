# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. #
celsius = float(input('Informe a temperatura, em Cº: '))
fahrenheit = (1.8*celsius) + 32
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF!'.format(celsius, fahrenheit))