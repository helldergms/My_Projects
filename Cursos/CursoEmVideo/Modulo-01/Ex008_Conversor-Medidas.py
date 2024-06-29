medida = int(input('Informe uma distância em metros: '))

print()
print(f'A medida de {medida:.1f}m corresponde a:\n'
      f'\n'
      f'{medida*0.001} kilômetro(s)\n' # calcular medida em kilômetro
      f'{medida*0.01} hectômetro(s)\n' # calcular medida em hectômetro
      f'{medida*0.1} decâmetro(s)\n' # calcular medida em decâmetro
      f'{medida*10} decímetro(s)\n' # calcular medida em decímetro
      f'{medida*100} centímetro(s)\n' # calcular medida em centímetro
      f'{medida*1000} milímetro(s)') # calcular medida em milímetro
