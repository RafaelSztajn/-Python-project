print('Bemvindo ao calculador de imc')
p = float(input('Entre com o seu peso!'))
a = float(input('entre com a sua altura'))
imc = p/(a*a)
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 < imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obsidade ')
elif imc > 40:
    print('Obesidade mórbida')
print('{:.2f}'.format(imc))