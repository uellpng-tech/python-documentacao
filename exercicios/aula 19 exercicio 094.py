pessoas = []
while True:

    con = input("Cadastrar nova pessoa S/N? ").upper()

    if con == "N":
        print("====================================================================================")
        print(f"O grupo tem {len(pessoas)} pessoas")

        tot = 0
        il = 0

        for i in pessoas:
            tot += pessoas[il]["idade"]
            il += 1
        print(f"A média de idade é {tot/len(pessoas)}")

        sl = []
        p = 0

        for mn in pessoas:
            if pessoas[p]["sexo"] == "F":
                sl.append(pessoas[p]["nome"])
            p += 1
        print(f"Mulheres no grupo {sl}")

        acm = []
        ps = 0

        print("Pessoas acima da média:")
        for im in pessoas:
            if pessoas[ps]["idade"] > tot/len(pessoas):
                acm.append(pessoas[ps])
            ps += 1

        for psm in acm:
            print(psm)

        break