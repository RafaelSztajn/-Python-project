import math


def fatorial(calcular, show):
    n = int(input('Qual é o numero que deseja fatorar ?'))
    m = math.factorial(n)
    show = m
    r = str(input('Deseja mostrar o valor ? [S/N]')).upper()[0]
    if r == 'S':
        for c in range(1, n + 1, 1):
            if c > 1:
                print('x', end='')
            print(' {}'.format(c, ), end=' ')
        print('= {}'.format(show))

    else:
        print('Obrigado por utilizar o programa')


fatorial('calcular', 'show')
