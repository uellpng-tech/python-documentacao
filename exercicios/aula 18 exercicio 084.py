dados = list()
pessoas = list()

while True:

    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()

    p_pesadas = []
    p_leves = []

    for p in pessoas:
        if p[1] >= 100:
            p_pesadas.append(p[0])
            p_pesadas.append(p[1])
        elif p[1] < 70:
            p_leves.append(p[0])
            p_leves.append(p[1])

    print(pessoas)

    c = input("Deseja continuar S/N: ").upper()

    if c == "N":
        print(f"Quantidade de pessoas cadastradas {len(pessoas)}\n Pessoas pesadas {p_pesadas} \n Pessoas leves {p_leves}")
        break
    elif c != "S":
        print("Apenas S ou N...")

    