m = [[], [], [], [], [], [], [], [], []]

l = 0
p = 0
pn = 0

for c in m:
    n = int(input(f"Digite o número da posição ({l},{p}) "))
    m[pn].append(n)
    p += 1
    pn += 1
    if p == 3:
        l += 1
        p = 0

print(f'''
        {m[0]} {m[1]} {m[2]}
        {m[3]} {m[4]} {m[5]} 
        {m[6]} {m[7]} {m[8]}
''')