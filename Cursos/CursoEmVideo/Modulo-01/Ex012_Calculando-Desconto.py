produto = float(input("Informe o preço do produto que será aplicado o desconto: R$ "))
desconto = produto - (produto*0.05)
print()
print(f'O preço inicial do produto sem desconto é R${produto:.2f}\n'
      f'Aplicando o desconto de 5% o valor final será de R${desconto:.2f}')
