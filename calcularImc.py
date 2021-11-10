peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f} e você está com obesidade'.format(imc))
else:
    print('Seu IMC é de {:.2f} e você esta com obesidade mórbida'.format(imc))
