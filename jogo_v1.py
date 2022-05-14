from funções import *
from dados import DADOS, EARTH_RADIUS


print(' ============================')
print('|                             |')
print('| Bem vindo ao Insper Países  |')
print('|                             |')
print(' ==== Design de Software ====\n') 
    
print('Comandos: \n')
print('          dica     - entra no mercado de dicas')
print('          desisto  - desiste da rodada\n')

print('Um país foi escolhido, tente adivinhar!')
print('Você tem 20 tentativas!\n')

tentativas = 20
cores_da_bandeira = []
cores_usadas = []
letras_capital = []
proibido = ['.', ',', '-', ';', ' ']
lista = []
distancias_dadas = []
i = 0
#FUNÇÕES
dic_normalizado = normaliza(DADOS)
escolhido = sorteia_pais(dic_normalizado)

palpite = str(input('Qual seu palpite? ')).lower().strip()
if palpite in dic_normalizado:
    tentativas -= 1
#BANDEIRA

for continente in DADOS:
                for pais in DADOS[continente]:
                    if pais == escolhido:
                        for cor,num in DADOS[continente][pais]['bandeira'].items():
                            if num > 0 :
                                if cor != 'outras':
                                    cores_da_bandeira.append(cor)

# CAPITAL

for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        capital = DADOS[continente][pais]["capital"]

#ÁREA

for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        area = DADOS[continente][pais]["area"]

#POPULAÇÃO

for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        pop = DADOS[continente][pais]["populacao"]

#CONTINENTE

for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        cont = continente

#LOOP
while tentativas > 0:
    if palpite not in dic_normalizado and palpite != 'dica':
        print('')
        print('país desconhecido')
    #DISTÂNCIA

    if palpite in dic_normalizado:

        #LAT/LONG PAÍS DO PALPITE

        for continente in DADOS:
            for pais in DADOS[continente]:
                if pais == palpite:
                    for geo,cords in DADOS[continente][pais]['geo'].items():
                        if geo == 'latitude':
                            latitude_palpite = cords
                        if geo == 'longitude':
                            longitude_palpite = cords

        #LAT/LONG PAÍS SORTEADO

        for continente in DADOS:
            for pais in DADOS[continente]:
                if pais == escolhido:
                    for geo,cords in DADOS[continente][pais]['geo'].items():
                        if geo == 'latitude':
                            latitude_escolhido = cords
                        if geo == 'longitude':
                            longitude_escolhido = cords
        dist = haversine(EARTH_RADIUS,latitude_escolhido,longitude_escolhido,latitude_palpite,longitude_palpite)
        lista.append([palpite,dist] )
        lista_ordenada = adiciona_em_ordem(palpite,dist,lista)
        distancias_dadas.append(dist)
        print('Distâncias: ')
        print(f'{palpite}: {distancias_dadas[i]:.3f} km')
        print('')
        print(f'Tentaivas: {tentativas}')
    if palpite == 'dica'.lower().strip():
        print('----------------------------------------\n 1. Cor da bandeira  - custa 4 tentativas\n 2. Letra da capital - custa 3 tentativas\n 3. Área             - custa 6 tentativas\n 4. População        - custa 5 tentativas\n 5. Continente       - custa 7 tentativas\n 0. Sem dica\n ----------------------------------------')
        dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        print('Distâncias:\n\n Dicas:')
    #DICA 0
        if dica_escolhida == 0:
            print('')
    #DICA 1
        if dica_escolhida == 1 and tentativas>0:
            while dica_escolhida == 1:
                if cores_da_bandeira == []:
                    print('Todas as cores já foram listadas!')
                    print(f'- {cores_usadas_str}\n')
                    print(f'Tentativas: {tentativas}')
                    break
                cor_sorteada = random.choice(cores_da_bandeira)
                cores_usadas.append(cor_sorteada)
                cores_da_bandeira.remove(cor_sorteada)
                cores_usadas_str=', '.join(cores_usadas)
                print(f'- {cores_usadas_str}\n')
                tentativas -= 4 
                print(f'Tentativas: {tentativas}')
                break
    #DICA 2
        if dica_escolhida == 2 and tentativas>0:
            while dica_escolhida == 2:
                letra_sorteada = sorteia_letra(capital,proibido)
                proibido += letra_sorteada
                print(capital)
                if len(letras_capital) == len(capital):
                    print('Todas as letras já foram dadas!\n')
                    print(f'- Letras da Capital: {letras_da_capital_str}\n')
                    print(f'Tentativas: {tentativas}')
                    break
                if letra_sorteada not in letras_capital:
                    letras_capital.append(letra_sorteada)
                letras_da_capital_str = ', '.join(letras_capital)
                print(f'- Letras da Capital: {letras_da_capital_str}\n')
                tentativas -= 3
                print(f'Tentativas: {tentativas}')
                break
    #DICA 3
        if dica_escolhida == 3:
            for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        area = DADOS[continente][pais]["area"]
                        print(f'Área: {area}')
                        tentativas -= 6
                        print(f'Tentativas: {tentativas}')
    #DICA 4
        if dica_escolhida == 4:
            for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        pop = DADOS[continente][pais]["populacao"]
                        print(f'População: {pop}')
                        tentativas -= 5
                        print(f'Tentativas: {tentativas}')
    #DICA 5
        if dica_escolhida == 5:
            for continente in DADOS:
                for pais in DADOS[continente] :
                    if pais == escolhido:
                        print(f'Continente: {continente}')
                        tentativas -= 7
                        print(f'Tentativas: {tentativas}')
    i += 1
    
    #print(f'- {cores_usadas_str}\n')
    #print(random.choice(capital))
    #print(f'Área: {area}')
    #print(f'População: {pop}')
    #print(f'Continente: {continente}')

    if palpite == escolhido:
        print('Muito Bem!')
        break

    if palpite == 'desisto':
        desistir = str(input('Tem certeza que deseja desistir da rodada? [s|n] '))
        if desistir == 's':
            print(f'>>> Que deselegante desistir, o país era: {escolhido}')
            break
        if desistir == 'n':
            print('')

    palpite = str(input('Qual seu palpite? ')).lower().strip()
    tentativas -= 1
    print(f'Tentativas: {tentativas}')

if tentativas == 0 or tentativas < 0:
    print('Suas tentativas acabaram :(')
    print(f'O país sorteado era {escolhido}\n')

fim_jogo = str(input('Deseja jogar novamente? [s/n] '))
if fim_jogo == 's':
    'jogar denovo'
if fim_jogo == 'n':
    print('Até a próxima!')