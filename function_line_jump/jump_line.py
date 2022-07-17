# A função deve solicitar um parâmetro, que será multiplicado para formar uma quebra de linha no terminal.

desenho = '###'


def jumpLine(desenho):
    desenho = desenho * 20
    return desenho


print(jumpLine(desenho))
