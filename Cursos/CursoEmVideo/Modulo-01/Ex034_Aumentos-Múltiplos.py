salarioFuncionario = float(input("Informe o valor do salário que será reajustado: "))

print()

if salarioFuncionario <= 1250:
    novoSalario = salarioFuncionario + (salarioFuncionario * 0.15)
    print(f'O salário atual informado é de R$ {salarioFuncionario:.2f}. Com reajuste de 15% passará a ser de R$ {novoSalario:.2f}')

else:
    novoSalario = salarioFuncionario + (salarioFuncionario * 0.10)
    print(f'O salário atual informado é de R$ {salarioFuncionario:.2f}. Com reajuste de 10% passará a ser de R$ {novoSalario:.2f}')
