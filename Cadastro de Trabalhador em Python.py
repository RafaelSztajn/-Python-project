nome = input('QUAL É O SEU NOME ?')
clt = int(input('Qual é o numero da sua CLT ? digite zero[0] caso não tenha'))
nascimento = int(input('Qual é o ano que você nasceu ?'))
trabalhador = {'Nome': nome, 'CLT': clt, 'Nascimento': nascimento}
if clt != 0:
    contrato = int(input('Em que ano você foi contratado ?'))
    salario = float(input('Quanto que é o seu salario ?'))
    trabalhador['Contrato'] = contrato
    trabalhador['Salario'] = salario
    trabalhador['Aposentadoria'] = contrato + 35
trabalhador['Idade'] = 2020 - nascimento
for e, v in trabalhador.items():
    print('{}: {}'.format(e, v))
