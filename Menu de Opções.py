n1=int(input('Primeiro valor'))
n2=int(input('Segundo valor'))
opção=0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção=int(input('Qual é a opção?'))
    if opção==1:
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif opção==3:
        if n1>n2:
            print(n1)
        if n2>n1:
            print(n2)
    elif opção == 2:
        print('{}x{}={}'.format(n1, n2, n1 * n2))
    elif opção == 4:
        print('Informe os numeros novamente')
        n1=int(input('Qual é o numero ?'))
        n2=int(input('Qual é o numero?'))

print('Fim do programa !!')







