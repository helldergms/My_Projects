from random import randint
from time import sleep


game = " Jogo da Adivinhação "

print(f'{"=" * 63}')
print(game.center(63, '='))
print(f'{"=" * 63}')
print('Estou pensando em um número entre 0 e 5... Consegue adivinhar?')

computador = randint(0, 5)

jogador = int(input("Digite seu palpite: "))

print()
print("PROCESSANDO...")
sleep(2.5)
print()

if jogador == computador:
    print("Parabéns, você ganhou!")

else:
    print("HaHaHa você perdeu!")
    print(f'Você escolheu {jogador} e eu pensei {computador}!')
