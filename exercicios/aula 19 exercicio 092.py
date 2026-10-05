dcapo = {}
dcapo["nome"] = input("Digite seu nome: ")
dcapo["idade"] = 2026 - int(input("Digite seu ano de nascimento: "))
dcapo["ctps"] = int(input("Digite sua carteira de trabalho (0 não tem): "))

campos = ["nome", "idade", "ctps", "contratação", "salário", "aposentadoria"]
cont = 0

if dcapo["ctps"] == 0:
    print("------------------------------------------------------------------------------------")
    print(dcapo)
    for p in campos:
        print(f"{p} tem valor {dcapo[p]}")
        cont += 1
        if cont == 3:
            break
else:
    dcapo["contratação"] = int(input("Digite seu ano de contratação: "))
    dcapo["salário"] = float(input("Digite seu salário: "))
    dcapo["aposentadoria"] = 65 - dcapo["idade"]
    print("------------------------------------------------------------------------------------")
    print(dcapo)
    for p in campos:
        print(f"{p} tem valor {dcapo[p]}")
