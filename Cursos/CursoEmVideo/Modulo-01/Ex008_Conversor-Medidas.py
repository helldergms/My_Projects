medida = int(input('Informe uma distância em metros: '))
print()
print(f'A medida de {medida:.1f}m corresponde a:\n'  # calculando medidas conforme apresentado abaixo
      f'\n'
      f'{medida*0.001} kilômetro(s)\n'
      f'{medida*0.01} hectômetro(s)\n'
      f'{medida*0.1} decâmetro(s)\n'
      f'{medida*10} decímetro(s)\n'
      f'{medida*100} centímetro(s)\n'
      f'{medida*1000} milímetro(s)')
