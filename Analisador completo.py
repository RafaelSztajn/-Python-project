id = 0
hidade = 0
nomevelho = ''
totm = 0
for c in range(1, 4 + 1):
    print('---------{}ºpessoa----'.format(c))
    nome = input('qual é o seu nome ?').strip()
    idade = int(input('Qual é a sua idade ?'))
    sexo = (input('M/F: ')).strip().upper()
    id = id + idade
    if c == 1 and sexo == 'M':
        hidade = idade
        nomevelho = nome
    if sexo == 'M' and idade > hidade:
        hidade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totm = totm+1
print('a media de idade foi de {}'.format(id / 4))
print(' o homen mais velho tem {} e o seu nome é {}'.format(hidade, nomevelho))
print('temos {} mulhere(s) no grupo'.format(totm))
