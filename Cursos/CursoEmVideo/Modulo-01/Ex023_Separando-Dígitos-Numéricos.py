numero = int(input("Digite um número de [0 a 9999]: "))

unidade = numero // 1 % 10

dezena = numero // 10 % 10

centena = numero // 100 % 10

milhar = numero // 1000 % 10

print()
print(f'Analisando o número {numero}')
print(f'Unidades: {unidade}')
print(f'Dezenas: {dezena}')
print(f'Centenas: {centena}')
print(f'Milhar: {milhar}')
