num = 0
while True:
    num = int(input('Entre com o numero'))
    if num < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, num * c))
