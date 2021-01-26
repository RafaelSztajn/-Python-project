soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor'))
    if num % 2 == 0:
        soma = soma + num
print('o valor da soma é {}'.format(soma))