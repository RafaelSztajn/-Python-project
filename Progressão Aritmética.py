termo1 = int(input('Primeiro termo'))
razão = int(input('Razão'))
decimo = termo1
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont<=total:
        print('{}-'.format(decimo),end='')
        decimo=decimo+razão
        cont+=1
    print('Pausa')
    mais=int(input('Quantos termos você quer mostrar a mais ?'))
print('PROGREÇÃO FINALIZADA COM {}TERMOS'.format(total))