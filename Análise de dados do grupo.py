idade = 0
sexo = ' '
cont = 0
cont2 = 0
cont3 = 0
while True:
    sexo = str(input('Qual é o seu sexo ?[M/F] ')).upper()
    idade = int(input('Quantos anos você tem? '))
    parada = input('Voce deseja parar ? [S/N]').upper()
    if idade >= 18:
        cont += 1
    if sexo == 'F':
        if idade < 20:
            cont2 += 1
    if sexo == 'M':
        cont3 += 1
    if parada == 'S':
        break
print('Você tem {} pessoas maiores de idade\n'
      'você tem {} Homens cadastrados\n'
      'você tem {} mulhere(s) abaixo de 20 anos cadastradas'.format(cont, cont2, cont3))
