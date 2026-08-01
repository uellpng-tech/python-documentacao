la = []
ponte = []
cont = 0

while True:
    ponte.clear()

    n = input("Nome aluno(a): ")
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    med = (n1+n2)//2

    ponte.append(cont)
    ponte.append(n)
    ponte.append(n1)
    ponte.append(n2)
    ponte.append(med)

    la.append(ponte[:])

    cont += 1

    c = input("Continuar S/N: ").upper()

    if c == "N":
        break

for d in la:
        print("Nu"," ", "Nome"," ", " ", "Média")
        print(f'{d[0]}    {d[1]}     {d[4]}')

while True:
    
    pe = int(input("Mostrar notas de qual aluno (999 interrompe): "))
    for c in range(0, len(la)):
        for num in la:
            if num[c] == pe:
                print(f"Nome {num[1]}, notas {num[2]}, {num[3]}")
                    
    if pe == 999:
        break