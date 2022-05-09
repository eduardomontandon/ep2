import random

def adiciona_em_ordem(pais, distancia, lista):
    nova_lista = []
    dados = [pais, distancia]
    if lista == []:
        nova_lista.append(dados)
    for i in lista:
        if i[1] < distancia:
            nova_lista.append(i)
        else:
            if dados not in nova_lista :
                nova_lista.append(dados)
            nova_lista.append(i)
    if dados not in nova_lista:
        nova_lista.append(dados)
    return nova_lista


def esta_na_lista(pais, lista):
    esta_na_lista = 0
    for i in lista:
        if i[0] == pais:
            esta_na_lista = 1
    if esta_na_lista == 1:
        return True
    else:
        return False


def sorteia_letra(palavra, lista):
    nova_palavra = ''
    for i in palavra:
        if i not in lista:
            nova_palavra += i
    return random.choice(nova_palavra)