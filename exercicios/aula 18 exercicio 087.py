m = [[], [], [], [], [], [], [], [], [], [], []]

l = 0
p = 0
pn = 0

for c in m[0:9]:
    n = int(input(f"Digite o número da posição ({l},{p}) "))

    if n % 2 == 0:
        m[9].append(n)
    
    m[pn].append(n)
    p += 1
    pn += 1

    if p == 3:
        m[10].append(n)
        
    if p == 3:
        l += 1
        p = 0


print(f'''
        {m[0]} {m[1]} {m[2]}
        {m[3]} {m[4]} {m[5]} 
        {m[6]} {m[7]} {m[8]}
''')

mai = m[3]

for ma in m[3:6]:
    if ma >= mai:
        mai = ma



print(f"A soma dos valores pares é {sum(m[9])}")
print(f"A soma dos valores da coluna três é {sum(m[10])}")
print(f"O maior valor da segunda linha é {mai}")