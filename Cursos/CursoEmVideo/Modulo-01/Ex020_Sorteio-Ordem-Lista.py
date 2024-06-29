from random import shuffle


print("ORDEM DE APRESENTAÇÃO DO TRABALHO ESCOLAR")

aluno_1 = str(input("Informe o nome do primeiro aluno: "))

aluno_2 = str(input("Informe o nome do segundo aluno: "))

aluno_3 = str(input("Informe o nome do terceiro aluno: "))

aluno_4 = str(input("Informe o nome do quarto aluno: "))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista_alunos)

print()
print(f'A Ordem dos alunos que apresentarão os trabalhos será:')
print(lista_alunos)
