# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
# considerando que cada litro pinta 2m²
tinta = area/2
print('Para pinturar essa parede, você irá precisar de {:.2f}L de tinta.'.format(tinta))