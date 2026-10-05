dcarreira = {}
dcarreira["nome"] = input("Digite seu nome: ")
dcarreira["partidas"] = int(input("Digite quantas partidas jogadas: "))
gols = []

for c in range(0, dcarreira["partidas"]):
    gols.append(int(input(f"Quantos gols na partida {c}? "))
)

dcarreira["gols"] = gols
print("=====================================================================")

qtg = 0 

for q in gols:
    qtg += q

dcarreira["total"] = qtg
campos = ["nome", "gols", "total"]

for l in campos:
    print(f"O campo {l} tem o valor {dcarreira[l]}")

print("=====================================================================")

print(f"O jogador {dcarreira['nome']} jogou {dcarreira['partidas']} partidas")

cont = 0

for c in dcarreira["gols"]:
    print(f"    Na partida {cont}, fez {c} gols")
    cont += 1
print(f"Foi um total de {dcarreira['total']} gols")