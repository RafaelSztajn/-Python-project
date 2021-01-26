print('velocidade do carro')
velocidade=int(input('entre com a velocidade do carro '))
multa=80
pagar=7
if velocidade>80:
    print('você ultrapassou o limete de velocidade \n e ira pagar {} reias pelo total de km '
          'ultrapasados '.format((velocidade-multa)*pagar))
else:
    print('a sua velocidade esta dentro das normas ')
