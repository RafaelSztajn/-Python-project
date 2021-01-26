def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um numero inteiro valido ')
        if ok:
            break
    return valor


n = leiaint('Digite um valor: ')
print('Você digitou o numero {}'.format(n))
