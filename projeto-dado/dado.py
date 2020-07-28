#Jogo de Dados

#***EM ANDAMENTO***

#Importações
#Randint para randomizar os lançamentos dos dados
#Sleep para dar uma pausa de um lançamento para o outro
from random import randint
from time import sleep

def jogo_dado():

    #Colhendo nome dos usuários 
    j1 = input('Nome do Primeiro Jogador: ')
    j2 = input('Nome do Segundo Jogador: ')

    print('Cada um jogará o dado 3x, a maior soma vence!\n')
    
    #Gerando jogadas do jogador 1
    total1 = 0
    for x in range(3):
        dado1 = randint(1, 6)
        total1 += dado1
        print(f'{j1.title()} jogou {dado1}')
        sleep(1)
    print(f'{j1.title()} totalizou {total1} pontos! Vez de {j2.title()}...\n')

    #Gerando jogadas do jogador 2
    total2 = 0
    for x in range(3):
        dado2 = randint(1, 6)
        total2 += dado2
        print(f'{j2.title()} jogou {dado2}')
        sleep(1)
    
    #Condições de vitória
    if total1 > total2:
        print(f'{j1.title()} Parabéns!!! Você venceu o jogo de {total1} a {total2}.\n')
    elif total2 > total1:
        print(f'{j2.title()} Parabéns!!! Você venceu o jogo por {total2} a {total1}.\n')

    jogar_novamente = input('Desejam jogar mais uma vez?[S/N] ')
    #Tratando possibilidades de erros de resposta do usuário
    while jogar_novamente.upper() != 'S' and jogar_novamente.upper() != 'N':
        print('Por favor, Responda com S ou N.')
        jogar_novamente = input('Deseja jogar mais uma vez?[S/N] ')
    if jogar_novamente.upper() == 'S':
        jogo_dado()
    else:
        print('Obrigado pela participação, até a próxima!')

jogo_dado()