valores = [18, 6, 26, 14]
print(valores[0])
# print(len(valores)) - tamanho
print(f'A lista tem {len(valores)} elementos')
valores.append(9) # add elemento
valores.sort()
print(valores)

# ajeitar
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'{c}, {v}')