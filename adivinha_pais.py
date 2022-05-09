import random
import math


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


def normaliza(dic_paises):
    dic_normalizado = {}
    dic_valor = {}
    for continente,paises in dic_paises.items():
        for pais,espec in paises.items():
            dic_valor = espec
            dic_valor['continente'] = continente
            dic_normalizado[pais] = dic_valor
    return dic_normalizado


def sorteia_pais(dicionario):
    lista = []
    for nome_pais in dicionario.keys():
        lista.append(nome_pais)
    pais_sorteado = random.choice(lista)
    return pais_sorteado


def haversine(raio,fi1,lambida1,fi2,lambida2):
    fi1r = math.radians(fi1)
    fi2r = math.radians(fi2)
    lambida1r = math.radians(lambida1)
    lambida2r = math.radians(lambida2)
    a = (math.sin((fi2r-fi1r)/2))**2
    b = math.cos(fi1r)*math.cos(fi2r)
    c = (math.sin((lambida2r-lambida1r)/2))**2
    distancia = 2*raio * math.asin((a + b*c)**0.5)
    return distancia