from random import randint

jogo = [1, 2]
numerossorteados = list()
vitoria = list()
verificarsorteio = list()
while verificarsorteio != jogo:
    cont = 0
    while True:
        sorteio = randint(1, 4)
        if sorteio not in numerossorteados:
            numerossorteados.append(sorteio)
            cont += 1
        if cont >= 2:
            break
    numerossorteados.sort()
    vitoria.append(numerossorteados[:])
    numerossorteados.clear()
    print(vitoria)
    verificarsorteio += vitoria
