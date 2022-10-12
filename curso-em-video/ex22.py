# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar /espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'''Seu nome com todas as letras maiúscula é {nome.upper()}.
Seu nome com todas as letras minúsculas é {nome.lower()}.
Seu nome tem, ao todo, {(len(nome))-(nome.count(' '))} letras.
Seu nome tem {len(nome.split())} palavras.
Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])}''')