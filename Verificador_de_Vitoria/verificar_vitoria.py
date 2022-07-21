from random import randint
from time import sleep


class classe:
    jogo = list([8, 10, 12, 13, 15])
    numerossorteados = list()
    y = 0
    i = 0
    while i <= 1:
        cont = 0
        while True:
            sorteio = randint(1, 25)
            if sorteio not in numerossorteados:
                numerossorteados.append(sorteio)
                cont += 1
            if cont >= 5:
                break
        numerossorteados.sort()
        print(numerossorteados)
        if numerossorteados[0] == jogo[0]:
            print(' -------- GOOOOOOOOOOOOOOLLLLLLLLLLLLLLLLLLL -----------')
        if numerossorteados != jogo:
            numerossorteados.clear()
            y += 1
            print(y)
        else:
            print(f'Foram feitos {y} jogos e você conseguiu.')
            print('Venceu!')
            break
