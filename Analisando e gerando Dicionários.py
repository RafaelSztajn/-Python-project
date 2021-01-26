def notas(*n, sit=False):
    """
    --> Função que analisa as notas de um aluno
    :param n:Notas de um aluno
    :param sit:valor opcinal para detalhar a nota de um aluno.
    :return:retorna o dicionario com varias informações
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5, 7, 9, 5, sit=True)
print(resp)
help(notas)
