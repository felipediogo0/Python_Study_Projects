preco = 30000
preco_lambda = 40000
preco_lista = [4000, 20000, 10000]


def calcular_imposto(preco):
    return preco * 0.3  # Para 30% de imposto


print(f'O imposta é de R$:{calcular_imposto(preco)}')


# A mesma função usando o método lambda

def calcular_imposto(preco_lambda): return preco_lambda * 0.3


print(f'O imposto a pagar, é de R$:{calcular_imposto(preco_lambda)}')

# Agora, iremos usar a função lambda para calcular uma lista, usando o método map.

impostos = list(map(lambda x: x*0.3, preco_lista))
print(impostos)
