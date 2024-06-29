largura = float(input("Informe a largura da parede em metros: "))

comprimento = float(input("Agora informe a altura da parede em metros: "))

área = largura * comprimento # calcular área total de um espaço

tinta = área / 2 # calcular quantidade de tinta que será usada no espaço

print()
print(f'Sua parede tem a dimensão de {largura:.2f}x{comprimento:.2f} e a área total é {área:.2f}m²')
print(f'Para pintar essa parede você precisará de {tinta:.2f}L de tinta.')
