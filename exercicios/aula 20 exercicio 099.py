import time

def linha():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def maior(*num):
    if len(num) == 0:
        linha()
        print("Analisando os valores...")
        time.sleep(0.5)
        print("Foram informados 0 números ao todo.")
        print("O número 0 é o maior valor.")
        time.sleep(0.5)
        linha()
    else:
        linha()
        print("Analisando os valores...")
        v = 0
        for m in num:
            print(m, end=" ", flush=True)
            time.sleep(0.5)
            v += 1
            ma = 0

            if m > ma:
                ma = m
        print(f"Foram informados {v} números ao todo.")
        print(f"O número {ma} é o maior valor.")
        time.sleep(0.5)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
