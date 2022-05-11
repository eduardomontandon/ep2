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

#FUNÇÕES
dic_normalizado = normaliza(DADOS)
escolhido = sorteia_pais(dic_normalizado)

if palpite == escolhido:
    print('Muito bem!')

if palpite != escolhido:
    print('O país escolhido era {}'.format(escolhido))
