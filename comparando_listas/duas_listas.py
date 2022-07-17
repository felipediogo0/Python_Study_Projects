lista1 = [5, 4, 3]
lista2 = [5, 3, 4]


def main():

    lista3 = []

    for i in lista1:
        for j in lista2:
            if(i == j):
                lista3.append(j)
                break
    print(lista3)


main()
