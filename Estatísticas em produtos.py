print('Seja bem vindo ao super barato!!')
produto = ' '
cont = totmil = menor = cont1 = 0
parada = ' '
barato = ' '
while True:
    produto = input('Qual é o nome do produto?')
    vp = float(input('Qual é o valor do produto ?'))
    parada = input('Você gostaria de parar o programa? [S/N]').upper()
    cont += vp
    cont1 += 1
    if vp > 1000:
        totmil += 1
    if cont1 == 1:
        menor = vp
        barato = produto
    else:
        if vp < menor:
            menor = vp
            barato = produto
    if parada == 'S':
        break
print('Você gastou com as suas compras um total de {}\n'
      'Você tem em sua bolsa de compras {} produtos acima de 1000 \n'
      'O produto mais barato é '.format(cont, totmil, ))
print('o produdo com o menor preço é o {} que é o {}'.format(menor, barato))
