print('=' * 30)
print('{:^30}'.format('Banco SZT'))
print('=' * 30)
valor = int(input('Qual valor você gostaria de sacar ?\n'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de cedulas {} cedulas de {}'.format(totced, ced))
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        if  ced == 20:
            ced = 10
        if  ced == 10:
            ced = 5
        if  ced == 5:
            ced = 2
        if  ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco SZt ...\n Tenha um bom dia !!')
