pares = []
impares = []
números = []

for c in range(0, 7):
    n = int(input(f"Digite o {c+1}º número: "))
    if n % 2 == 0:
        pares.append(n)
        números.append(pares[:])
        pares.clear()
    else:
        impares.append(n)
        números.append(impares[:])
        impares.clear()

números.append(pares[:])
números.append(impares[:])

pos = 1

for n in números[0]:
    if n > números[0][pos]:
        insert.

print(números)