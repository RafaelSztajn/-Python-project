p0 = int(input('Qual é o valor ?'))
p1 = int(input('Qual é o valor ?'))
p2 = int(input('Qual é o valor ?'))
p3 = int(input('Qual é o valor ?'))
p4 = int(input('Qual é o valor ?'))
n = [p0, p1, p2, p3, p4]
print(n)
for i, v in enumerate(n):
    if v == max(n):
        print('O maior valor  está na posiçãoi {} que é igual a {}'.format(i, max(n)))
    if v == min(n):
        print('O menor valor está na posição {} que é igual a {}'.format(i, min(n)))
