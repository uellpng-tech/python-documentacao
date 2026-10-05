jogadores = []
while True:
    jogador = {}
    jogador["jogador"] = input("Digite seu nome: ")
    jogador["partidas"] = int(input(f"Digite quantas partidas {jogador['jogador']} jogou: : "))
    gols = 0
    golsp = []
    for c in range(0, jogador["partidas"]):
        gol = int(input(f"Quantos gols na partida {c}: "))
        gols += gol
        golsp.append(gol)
    jogador["golst"] = gols
    jogador["gols"] = golsp

        
    jogadores.append(jogador)

    pes = ""

    c = input("Deseja continuar S/N: ").upper()
    if c == "N":
        pl = 0
        for p in jogadores:
            print(f"{pl} {jogadores[pl]["jogador"]} {jogadores[pl]["gols"]} {jogadores[pl]["golst"]}")
            pl += 1
        print("======================================================================")
        
        while pes != 999:

            pes = int(input("Mostrar dados de qual jogador (999 para parar)? ").upper())
            print("======================================================================")
            print(f"Levantamento do jogador {jogadores[pes]["jogador"]}:")
            gl = 0
            for g in jogadores[pes]["gols"]:
                print(f"No jogo {gl} fez {g} gols.")
                gl += 1

        break
        
    else:
        print("======================================================================")