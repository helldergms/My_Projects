nome = str(input("Digite seu nome completo: ")).strip().title()

dividido = nome.split()

print()
print("Analisando seu nome...")
print(f'Seu nome completo com iniciais maiúsculas fica {nome}')
print(f'Seu nome completo em maiúscula fica {nome.upper()}')
print(f'Seu nome completo em minúscula fica {nome.lower()}')
print(f'Seu nome completo possui {len(nome) - nome.count(' ')} letras no total')
print(f'Seu primeiro nome é {dividido[0]} e possui {len(dividido[0])} letras')
