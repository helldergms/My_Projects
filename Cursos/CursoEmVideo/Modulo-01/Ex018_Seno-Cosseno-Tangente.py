from math import radians, sin, cos, tan
angulo = float(input("Informe o ângulo que deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print()
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
