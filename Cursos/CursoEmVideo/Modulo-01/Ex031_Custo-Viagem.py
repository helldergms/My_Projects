distancia_viagem = float(input("Informe a distância da sua viagem: "))

print(f'Você está prestes a realizar uma viagem de {distancia_viagem:.1f} KM!')
print()

if distancia_viagem <= 200:
    tarifa_passagem = distancia_viagem * 0.50
    
    print(f'O preço da sua passagem para esta viagem de {distancia_viagem:.1f} KM custará R$ {tarifa_passagem:.2f}')
    print("Tenha uma boa viagem!")
    print()

else:
    tarifa_passagem = distancia_viagem * 0.45
    
    print(f'O preço da sua passagem para esta viagem de {distancia_viagem:.1f} KM custará R$ {tarifa_passagem:.2f}')
    print("Tenha uma boa viagem!")
    print()