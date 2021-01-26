tabela='quejo','3,0','presunto','5,00','cerveja','4,00','cereja','7,00'
print(' o valor do produto {} custa {}'.format(tabela[0],tabela[1]))
print(' o valor do produto {} custa {}'.format(tabela[2],tabela[3]))
print(' o valor do produto {} custa {}'.format(tabela[4],tabela[5]))
print(' o valor do produto {} custa {}'.format(tabela[6],tabela[7]))

print('-'*40 + f'\n{"LISTAGEM DE PREÇOS":^40}\n' + '-'*40)
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
for item in range(0, len(lista),2):
    print('-'*40)
    print('{:.<30} {:>6.2f}'.format(lista[item],lista[item+1]))
