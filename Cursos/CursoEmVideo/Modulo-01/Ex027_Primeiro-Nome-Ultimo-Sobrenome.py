nome = str(input("Digite seu nome completo: ")).strip().title()
lista_nome = nome.split()
primeiro_nome = lista_nome[0]
ultimo_sobrenome = lista_nome[-1]
print()
print("Muito prazer em te conhecer!")
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último sobrenome é {ultimo_sobrenome}')
