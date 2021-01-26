ano=int(input('entre com o ano que desejar '))
num=ano+4
if num//4==num/4 and ano%100!=0 or ano% 400==0:
    print('esse ano  é bissexto')
else:
    print('esse ano não é bissexto')



