triangulo01=float(input('Entre com o primeiro  lado do triangulo '))
triangulo02=float(input('entre com o segundo lado do triangulo '))
triangulo03=float(input('entre com o terceiro lado do triangulo '))
if triangulo01==triangulo02==triangulo03:
    print('equilatero ')
elif triangulo01!=triangulo02!=triangulo03 and triangulo02!=triangulo01!=triangulo03 \
      and triangulo03!=triangulo02!=triangulo01:
    print('escaleno ')
elif triangulo01==triangulo02 and  triangulo03!=(triangulo01,triangulo02):
    print('isóceles')
elif triangulo01==triangulo03 and triangulo02!=(triangulo01,triangulo03):
    print('isoceles')
elif triangulo02==triangulo03 and triangulo01!=(triangulo02,triangulo03):
    print('isoceles')