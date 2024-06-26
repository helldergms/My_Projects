nome = str(input("Informe o seu nome completo: ")).strip().upper()
lista_nome = nome.split()
sobrenome = lista_nome.count('SILVA')
print(f'Seu nome tem SILVA? {sobrenome == True}')
