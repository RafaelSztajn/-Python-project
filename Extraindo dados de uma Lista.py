lista = []
cont = 0
n = 0
while True:
    n = int(input('Qual valor você deseja ?'))
    lista.append(n)
    cont += 1
    s = str(input('Deseja continuar ?N/S')).upper()
    if s == 'N':
        break
lista.sort(reverse=True)
if 5 not in lista:
    print('O valor 5 não está na lista')
else:
    print('O valor 5  esta na lista ')
print('A ordem reversa de numeros é {} e foram digitados {} numeros'.format(lista, cont))
