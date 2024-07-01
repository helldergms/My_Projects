valor1 = int(input("Digite o primeiro valor: "))

valor2 = int(input("Digite o segundo valor: "))

valor3 = int(input("Digite o terceiro valor: "))

menorValor = maiorValor = valor1

if valor2 > valor1 and valor2 > valor3:
    maiorValor = valor2

if valor3 > valor1 and valor3 > valor2:
    maiorValor = valor3

if valor2 < valor1 and valor2 < valor3:
    menorValor = valor2

if valor3 < valor2 and valor3 < valor1:
    menorValor = valor3

print()
print(f'O MENOR valor digitado foi {menorValor}')
print(f'O MAIOR valor digitado foi {maiorValor}')
