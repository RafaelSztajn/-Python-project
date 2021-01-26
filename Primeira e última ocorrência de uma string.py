frase=input('entre com uma frase ')
a=frase.count('a')
b=frase.find('a')
c=frase.rfind('a')
print('o numero de letras ´a´ é {}\n'
      ' ela aparece primeiro na posição{}\n '
      'a sua ultima posição é {}'
      .format(a,b,c))
