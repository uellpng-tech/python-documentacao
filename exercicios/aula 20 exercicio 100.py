import random
import time

numeros = []

def soma():
    n = 0
    for num in numeros:
        if num%2 == 0:
            n += num
    print(f"Somando os valores pares de {numeros}, temos {n}")

def sorteia():
    print("Sorteando 5 valores da lista:", end=" ")
    while len(numeros) != 5:
        numeros.append(random.randint(1, 5))
    for num in numeros:
        print(num, end=" ", flush=True)
        time.sleep(0.5)
    print("Pronto!")
    soma()
    
        
sorteia()