import random
import time
from operator import itemgetter

jogadores = {}

for c in range(1,5):
    numd = random.randint(1, 6)
    time.sleep(0.5)
    print(f"jogador{c} tirou {numd}")
    jogadores[f"jogador{c}"] = numd

print("---------------ranking---------------")

rank = {}
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f"{i+1} lugar {v[0]} com {v[1]}")
    time.sleep(0.5)