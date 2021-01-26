variavel = []
v2 = []
maior = menor = 0
while True:
    n = str(input('Qual é o seu nome ?'))
    p = float(input('Qual é o seu peso ?'))
    variavel.append(n)
    variavel.append(p)
    if len(v2) == 0:
        maior = menor = variavel[1]
    else:
        if variavel[1] > maior:
            maior = variavel[1]
        if variavel[1] < menor:
            menor = variavel[1]
    v2.append(variavel[:])
    variavel.clear()
    s = str(input('Deseja continuar ?N/S')).upper()
    if s == 'N':
        break
print(v2)
print('Ao Total tivemos {} '.format(len(v2)))
print('O maior peso foi {} '.format(maior), end='')
print('o menor peso foi {} '.format(menor), end='')
for p in v2:
    if p[1] == maior:
        print(p[0], end='')
for p in v2:
    if p[1] == menor:
        print(p[0], end='')
