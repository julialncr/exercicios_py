'''
--------------------------------
| Exercício 1 - Funções        |
| Por: Julia Dias              |
--------------------------------
'''


def lista():
    import random
    import sys

    tamanho = sys.argv[1]
    lista_aleatoria = random.sample(range(1, 11), int(tamanho))
    print(lista_aleatoria)

lista()

