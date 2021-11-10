produto = float(input('Digite o valor do produto: R$ '))
pagamento = int(input('Qual forma de pagamento:\n'
                      '1 - Dinheiro/Cheque \n'
                      '2 - Cartão de Crédito\n'))
if pagamento == 1:
    v_final = produto - (produto * 10 / 100)
    print('O valor do produto saiu com um desconto de 10%. Portanto o valor pago é de:'
          'R${:.2f}'.format(v_final))
elif pagamento == 2:
    qtd = int(input('Quantas vezes?\n'))
    if qtd == 1:
        v_final = produto - (produto * 5 / 100)
        print('Você escolheu pagar em 1x portanto terá 5% de desconto e o valor a ser pago é de:'
              'R${:.2f}'.format(v_final))
    elif qtd == 2 :
        v_final = produto / 2
        print('Você escolheu pagar em 2x portanto cada parcela será de R${:.2f}'.format(v_final))
    elif qtd > 2:
        v_final = produto + (produto * 20 / 100)
        parcela = v_final / qtd
        print('Você escolheu pagar em {}x portanto terá 20% de juros\n'
              'o produto sairá por R${:.2f} e cada parcela será de R${:.2f}'
              ''.format(qtd, v_final, parcela))
else:
    print('A opção digitada não é válida')