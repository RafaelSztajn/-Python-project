print('Seja bem vindo a locadora de automoveis')
dias = int(input('quantos dias durou o aluguel? '))
km = float(input('Quantos km foram percorridos? '))
custo = km*0.15
fixo = 60
print('o seu aluguel durou {} dias'.format(dias))
print('você andou {}km e gastou {} reais'.format(km, custo))
print('a sua fatura ficou em {} reais +{} reais fixos totalizando {} reais'.format(custo, fixo, custo+fixo))
