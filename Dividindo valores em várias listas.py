lista0=[]
lista1=[]
lista2=[]
while True:
    n=int(input('Qual é o valor ?'))
    lista0.append(n)
    s = str(input('Deseja continuar ?N/S')).upper()
    if s == 'N':
        break
for i,v in enumerate(lista0):
    if v%2==0:
        lista1.append(v)
    else:
        lista2.append(v)
print(lista0)
print(lista1)
print(lista2)
