import math
print('bem vindo a matemática')
cateto_oposto = int(input('entre com o cateto oposto '))
cateto_adj = int(input('entre com o cateto adj '))
cato = math.pow(cateto_oposto,2)
cata = math.pow(cateto_adj,2)
hip = cata+cato
print('O valor da hipotenuza é igual a {}'.format(math.sqrt(hip)))

