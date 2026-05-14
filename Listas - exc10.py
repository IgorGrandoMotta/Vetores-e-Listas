tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

jogador = "X"

for rodada in range(9):
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

    posicao = int(input("Jogador " + jogador + ", escolha uma posição (0 a 8): "))
    tabuleiro[posicao] = jogador

    venceu = False

    if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador:
        venceu = True
    if tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador:
        venceu = True
    if tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador:
        venceu = True
    if tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador:
        venceu = True
    if tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador:
        venceu = True
    if tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador:
        venceu = True
    if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
        venceu = True
    if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
        venceu = True

    if venceu:
        print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
        print("---------")
        print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
        print("---------")
        print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
        print("Jogador", jogador, "venceu!")
        break

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

else:
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print("Empate!")