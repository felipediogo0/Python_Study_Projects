from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quanto jogos vamos fazer?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Os números sorteados foram {l}')
    sleep(1)
