velocidade_carro = int(input("Informe a velocidade registrada: "))
limite_velocidade = 80
multa = (velocidade_carro - limite_velocidade) * 7
print()
if velocidade_carro > limite_velocidade:
    print(f"Você ultrapassou o limite máximo permitido da via de 80 KM/h!")
    print(f'Seu veículo foi flagrado rodando a {velocidade_carro} KM/h e será multado em R$ {multa:.2f} pelo excedente de velocidade!')
    print()

else:
    print("Veículo circulando dentro do limite permitido!")
    print()
    