nome=input('Seja bem vindo qual é o seu nome ?')
emprestimo=float(input('Qual é o valor do emprestimo {} ?'.format(nome)))
salario=float(input('Quanto você ganha sr(a){} ?'.format(nome)))
tempo=int(input('Quanto tempo para quitar o emprestimo ? '))
prestação=emprestimo/tempo
conta= prestação/3.333
if salario>conta:
    print('Parabens o seu credito foi aprovado!')
    print('O parcelamento ficou em {} meses de R${:.2f} por mês '.format(tempo,prestação))
elif salario<conta:
    print('O credito não foi aprovado')

