from random import randint
print('=+'*20)
print('{:^40}'.format(' Vamos jogar Jokenpô!!! '))
print('=+'*20)
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input('O que você vai escolher?\n'
                    '[ 0 ] Pedra;\n'
                    '[ 1 ] Papel;\n'
                    '[ 2 ] Tesoura\n'))
if jogador < 0 or jogador > 2:
    print('Opção errada!! Tente novamente!')
elif jogador == computador:
    print('Você escolheu {} e o computador {} portanto deu empate'
          ''.format(itens[jogador], itens[computador]))
elif jogador == 1 and computador == 0:
    print('Você escolheu {} e o computador {} portanto você ganhou!! Parabens!!!'
          ''.format(itens[jogador], itens[computador]))
elif jogador == 2 and computador == 1:
    print('Você escolheu {} e o computador {} portanto você ganhou!! Parabens!!!!'
          ''.format(itens[jogador], itens[computador]))
elif jogador == 0 and computador == 2:
    print('Você escolheu {} e o computador {} portanto você ganhou!! Parabens!!!!'
          ''.format(itens[jogador], itens[computador]))
else:
    print('Você escolheu {} e o computador {} Ahhhh!!! você perdeu!!!'
          ''.format(itens[jogador], itens[computador]))
