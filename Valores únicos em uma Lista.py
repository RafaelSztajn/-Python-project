numeros=list()
while True:
    n=int(input('Qual é o valor que você deseja ?'))
    if n not in numeros:
        numeros.append(n)
        print('NUMERO ADD COM SUCESSO!!')
    else:
        print('Valor duplicado , não posso adicionar!!')

    p=str(input('Deseja continuar?')).upper()[0]
    if p=='N':
        break
numeros.sort()
print(numeros)
