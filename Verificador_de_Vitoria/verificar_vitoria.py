from random import randint

jogo = list([1, 2])
numerossorteados = list()
i = 0
while i <= 1:
    cont = 0
    while True:
        sorteio = randint(1, 4)
        if sorteio not in numerossorteados:
            numerossorteados.append(sorteio)
            cont += 1
        if cont >= 2:
            break
    numerossorteados.sort()
    print(numerossorteados)
    if numerossorteados != jogo:
        numerossorteados.clear()
    else:
        print('Venceu!')
        break
