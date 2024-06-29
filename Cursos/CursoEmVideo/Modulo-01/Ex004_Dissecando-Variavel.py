teste = input("Digite algo: ")

print()

print(f'O tipo primitivo deste valor é {type(teste)}.') # identificar o tipo da variável
print(f'É alfanumérico? {teste.isalnum()}') # identificar se é alfanumérico
print(f'É alfabético? {teste.isalpha()}') # identificar se é alfabético
print(f'Está em minúsculo? {teste.islower()}') # identificar se está em minúsculo
print(f'Está em maiúsculo? {teste.isupper()}') # identificar se está em maiúsculo
print(f'É um número? {teste.isnumeric()}') # identificar se é um número
print(f'Só tem espaços? {teste.isspace()}') # identificar se tem apenas espaços
print(f'Está capitalizado?(primeira letra em maiúscula) {teste.istitle()}') # identificar se a primeira letra de cada palavra está em maiúscula
