num = [[], []]
valor = 0
for c in range(1, 7 + 1):
    valor = int(input('Digite o {}º valor!'.format(c)))
    if valor % 2 == 1:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('=-' * 30)
print('Todos os valores são {}'.format(num))
