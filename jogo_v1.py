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

palpite = str(input('Qual seu palpite? ')).lower().strip()
tentativas = 20
cores_da_bandeira = []
i = 0
a = 0
#FUNÇÕES
dic_normalizado = normaliza(DADOS)
escolhido = sorteia_pais(dic_normalizado)
#LOOP
#while palpite != escolhido:
if palpite not in dic_normalizado:
    print('')
    print('país desconhecido')
if palpite == 'dica'.lower().strip():
    print('----------------------------------------\n 1. Cor da bandeira  - custa 4 tentativas\n 2. Letra da capital - custa 3 tentativas\n 3. Área             - custa 6 tentativas\n 4. População        - custa 5 tentativas\n 5. Continente       - custa 7 tentativas\n 0. Sem dica\n ----------------------------------------')
    dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
    if dica_escolhida == 0:
        print('')
        palpite = str(input('Qual seu palpite? ')).lower().strip()
    if dica_escolhida == 1:
        'achar cor da bandeira'
    if dica_escolhida == 2:
        'sortear letras da capital'
    if dica_escolhida == 3:
        'área do país'
    if dica_escolhida == 4:
        'população do país'
    if dica == 5:
        'continente em que o país esta inserido'

palpite = str(input('Qual seu palpite? ')).lower().strip()
