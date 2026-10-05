alunodc = {}

n = input("Digite seu nome: ")
alunodc["aluno"] = n
m = int(input("Digite sua média: "))
alunodc["média"] = m

if alunodc["média"] < 7:
    alunodc["situação"] = "reprovado"
else:
    alunodc["situação"] = "aprovado"

print(f"O aluno {n} foi {alunodc["situação"]}, sua média foi {m}")