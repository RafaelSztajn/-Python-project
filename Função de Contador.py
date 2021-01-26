def contador(alfa):
    q = int(input('qual é o inicio?'))
    f = int(input('qual é o final ?'))
    if f == 0:
        f = -2
    p = int(input('qual é o o passo?'))
    for c in range(q, f + 1, p):
        print('{}'.format(c), end=' ')


def pronto(q):
    print('Contando de 10 até 0 temos: ')
    for d in range(10, -1, -2):
        print('{}'.format(d), end=' ')
    print()
    print('Contando de 1 ate 0 temos:')
    for w in range(1, 11, 1):
        print('{}'.format(w), end=' ')
    print()


pronto('q')
contador('alfa')
