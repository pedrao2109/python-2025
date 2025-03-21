num = 0
soma = 0
boletim = []
nome = []
media = []
for p in range(num,4):
    desmpenho_aluno = tuple()
    nota = []
    i = 0
    nome = (input(f"Digite o nome {num+1}º alunos: "))
    for s in range(1,4):
        nota.append(int(input(f"Informe a {num+1}º nota: ")))
        i = i + 1
    nota.append(sum(nota)/4)
    desmpenho_aluno = nome, nota
    boletim.append(desmpenho_aluno)
    num = num + 1
for b in boletim:
    print(' ')
    print(f"Aluno {b[0]} com media {b[1][-1]}")
    print(' ')