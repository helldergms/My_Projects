from random import choice


aluno_1 = str(input("Informe o nome do primeiro aluno: "))

aluno_2 = str(input("Informe o nome do segundo aluno: "))

aluno_3 = str(input("Informe o nome do terceiro aluno: "))

aluno_4 = str(input("Informe o nome do quarto aluno: "))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

escolhido = choice(lista_alunos)

print()
print(f'O(A) aluno(a) escolhido(a) para apagar o quadro foi o(a) {escolhido}')
