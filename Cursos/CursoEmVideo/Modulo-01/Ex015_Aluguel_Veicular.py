diaria_aluguel = int(input('Informe a quantidade de dias para locação do veículo: '))

valor_diaria = 60 # variável do preço da diária

aluguel_veiculo = diaria_aluguel * valor_diaria # cálculo da diária da locação do veículo

quilometros_rodados = float(input('Informe a quantidade de KM rodados: '))

valor_quilometro = 0.15 # variável da tarifa por quilômetro

custo_quilometro = quilometros_rodados * valor_quilometro # cálculo do custo por quilômetro rodado

total = aluguel_veiculo + custo_quilometro # cálculo do valor total a pagar

print()
print(f'Você alugou o veículo por {diaria_aluguel} dias e pagará R$ {aluguel_veiculo:.2f}')
print(f'Você rodou {quilometros_rodados} Km e pagará R$ {custo_quilometro:.2f}')
print(f'O valor total a pagar da locação + km rodados é de R$ {total:.2f}')
