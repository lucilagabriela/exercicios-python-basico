# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# km hm dam m dm cm mm

metros = float(input('Uma distância em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(metros, km, hm, dam, dm, cm, mm))