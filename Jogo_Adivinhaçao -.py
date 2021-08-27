from random import randint
from time import sleep
resp1 = 'Sim'.upper()[0]
resp2 = 'Não'.upper()[0]
computador = randint(0, 100)
print('Olá, sou seu computador, vamos jogar?')
pergunta = str(input('E aí, vamos? [Sim/Não]: ')).strip() .upper()[0]
acertou = False
palpites = 0
if pergunta == resp2:
    print('Okay, quem sabe na próxima, Até Logo.')
elif pergunta == resp1:
    print('Okay, Então vamos nessa. ')
    print('Você terá 10 tentativas, Boa sorte. ')
    print('CARREGANDO O JOGO, AGUARDE...')
    sleep(2)
    print('=' * 26)
    print('{:^26}'.format('Jogo da Adivinhação'))
    print('=' * 26)
    while not acertou:
        jogador = int(input('Digite um número entre 0 e 100: '))
        print('PROCESSANDO...')
        sleep(1.5)
        palpites += 1
        if jogador == computador:
            acertou = True
            print(f'Parabéns você ganhou depois de {palpites} tentativas.')
        elif palpites >= 10:
            acertou = True
            print('GAME OVER.')
        elif jogador < computador:
            print('O número é MAIOR, Tente novamente.')
        elif jogador > computador:
            print('O número é MENOR, Tente novamente.')
