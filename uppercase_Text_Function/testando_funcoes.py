# Lista de nomes, com strings maiusculas e minusculas

produtos = ['ABCDE3323', '  aBcdEE3424    ', 'abcdef213   ', 'AbdAEf2123']

texto = "absDkj302"

# Aqui vamos declarar a função, que deve ler o texto e devolver em letras maiúsculas e sem espaçamentos.
# texto aqui é um parâmetro de função, que deverá ser substituído por outra variável, ao aplicarmos a mesma função em outro local.


def uppercaseText(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto


# Aqui eu fi tudo em uma única linha. Usei o 'f' para concatenação, chamei o texto e depois o mesmo texto, dentro da função(tratar_texto).
print(
    f'Seu texto era assim {texto} e agora, ficou assim: {uppercaseText(texto)}.')

# Agora, faremos um laço for para que a fução, percorra uma lista e faça o processo de UpperCase.
# Aqui, eu criei uma nova variável produtos1, para salvar com o metodo list(), a lista antes da execução do laço de formatação.
produtos1 = list(produtos)
for i, produto in enumerate(produtos):
    produtos[i] = uppercaseText(produto)
print(f'Sua lista era assim: {produtos1} e ficou agora, assim: {produtos}')
