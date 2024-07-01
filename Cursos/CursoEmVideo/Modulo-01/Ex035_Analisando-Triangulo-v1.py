titulo = " Analisador de Triângulo "

print(titulo.center(50, "="))

reta1 = float(input("Informe o valor do primeiro segmento: "))

reta2 = float(input("Informe o valor do segundo segmento: "))

reta3 = float(input("Informe o valor do terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima PODEM formar um triângulo!")

else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")
    