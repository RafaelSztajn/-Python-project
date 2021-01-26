programa=input('Qual é o seu nome ?').strip()
frase=('{}'.format(programa))
maiusculo=frase.upper()
minusculo=frase.lower()
divisor=frase.split()
div=divisor[0]
total=len(frase)-frase.count(' ')
print('{}\n{}\n{}\n{}'.format(maiusculo,minusculo,total,div))










