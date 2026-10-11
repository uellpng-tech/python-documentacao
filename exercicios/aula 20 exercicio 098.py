import time

def linha():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def contador(ini, passo, fim):
    linha()
    print("Contagem de 1 até 10 de 1 em 1")
    for c in range(1,11):
        print(c, end=" ", flush=True)
        time.sleep(0.5)
    print("Fim!")
    linha()
    print("Contagem de 10 até 0 de 2 em 2")
    i = 12
    while i > 0:
        i -= 2
        print(i, end=" ", flush=True)
        time.sleep(0.5)
    print("Fim!")
    linha()
    print("Agora é sua vez!!!")
    ini = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    if passo == 0:
        passo = 1
    linha()
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}")
    if ini > fim:
        i = ini
        while i > fim:
            i -= passo
            print(i, end=" ", flush=True)
            time.sleep(0.5)
        print("Fim!")
        linha()
    elif ini < fim:
        for c in range(ini, fim+1, passo):
            print(c, end=" ", flush=True)
            time.sleep(0.5)
        print("Fim!")

contador(0, 0, 0)