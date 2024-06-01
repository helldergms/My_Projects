real = float(input("Informe quantos reais você deseja fazer câmbio R$ "))
cambioReal = real / 5.25
print(f'Com R${real:.2f} você consegue comprar US${cambioReal:.2f}!')
print()
dolar = float(input("Informe quantos dólares você deseja fazer câmbio US$ "))
cambioDolar = dolar * 5.25
print(f'Com US${dolar:.2f} você consegue comprar {cambioDolar:.2f}')
