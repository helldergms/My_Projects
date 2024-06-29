numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))

soma = numero1 + numero2 # calcular soma

subtracao = numero1 - numero2 # calcular subtração

multiplicacao = numero1 * numero2 # calcular multiplicação

divisao = numero1 / numero2 # calcular divisão

divisaoInteira = numero1 // numero2 # calcular divisão inteira

restoDivisao = numero1 % numero2 # calcular resto de uma divisão inteira

exponencial = numero1 ** numero2 # calcular exponencial

print()

print(f'A soma entre {numero1} e {numero2} é igual a {soma}.')
print(f'A subtração é {subtracao}.\nA multiplicação é {multiplicacao}.\nA divisão é {divisao:.2f}.')
print(f'A divisão inteira é {divisaoInteira}.\nO resto da divisão é {restoDivisao}.\nO exponencial é {exponencial}.')