salarioInicial = float(input("Informe o valor atual do salário que será reajustado: R$ "))

reajuste = salarioInicial + (salarioInicial * 0.15) # calcular reajuste de salário em 15%

print()
print(f'O trabalhador informou salário atual de R${salarioInicial:.2f}')
print(f'Com o reajuste de 15%, o salário deste trabalhador passará a ser de R${reajuste:.2f}')
