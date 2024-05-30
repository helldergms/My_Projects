numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisaoInteira = numero1 // numero2
restoDivisao = numero1 % numero2
exponencial = numero1 ** numero2
print()
print(f'A soma entre {numero1} e {numero2} é igual a {soma}.')
print(f'A subtração é {subtracao}.\nA multiplicação é {multiplicacao}.\nA divisão é {divisao:.2f}.')
print(f'A divisão inteira é {divisaoInteira}.\nO resto da divisão é {restoDivisao}.\nO exponencial é {exponencial}.')