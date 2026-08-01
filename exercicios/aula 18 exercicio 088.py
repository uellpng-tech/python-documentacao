import random

np = int(input("Quantos palpites: "))
p = [[random.randint(1, 60) for c in range(0, 6)] for l in range(np)]

po = 0

for pa in p:
    po += 1
    print(f"Palpite {po}º: {pa}")