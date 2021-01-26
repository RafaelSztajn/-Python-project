print('Seja bem vindo a smart center !!')
print('Escolha o produto que desejar \n 1  para ps4 \n 2 para xbox\n 3 para iphone\n')
ex = int(input(':'))

if ex == 1:
    print('você escolheu o ps4 ')
    print('esse produto custa R$1500')
    print("Digite 1 para\n à vista no dinheiro/cheque 10% de desconto\ndigite 2 para"
          "\nà vista no cartão 5% de desconto\ndigite 3 para\nem 2x no cartão: preço normal"
          "\ndigite 4 para 3x ou mais no cartão com 20% de juros")
    b = int(input('Qual seria a forma de pagamento?'))
    if b == 1:
        print('você ira pagar pelo seu ps4 R${} obrigado pela preferencia!!'.format(1500 - 1500 / 10))
    if b == 2:
        print('você ira pagar pelo seu ps4 R${:.2f} obrigado pela preferencia!!'.format(1500 - 1500 / 20))
    if b == 3:
        print('você ira pagar pelo seu ps4 2x de R${} obrigado pela preferencia!!'.format(1500 / 2))
    if b == 4:
        x = int(input('Em quantas vezes? '))
        z = 1500 / 5
        print('voce ira pagar pelo seu ps4 {}x de R${} obrigado pela preferencia!'.format(x, (1500 / x) + z / x))
if ex == 2:
    print('você escolheu o xbox ')
    print('esse produto custa R$2000')
    print("Digite 1 para\n à vista no dinheiro/cheque 10% de desconto\ndigite 2 para"
          "\nà vista no cartão 5% de desconto\ndigite 3 para\nem 2x no cartão: preço normal"
          "\ndigite 4 para 3x ou mais no cartão com 20% de juros")
    b = int(input('Qual seria a forma de pagamento?'))
    if b == 1:
        print('você ira pagar pelo seu xbox R${} obrigado pela preferencia!!'.format(2000 - 2000 / 10))
    if b == 2:
        print('você ira pagar pelo seu xbox R${:.2f} obrigado pela preferencia!!'.format(2000 - 2000 / 20))
    if b == 3:
        print('você ira pagar pelo seu xbox 2x de R${} obrigado pela preferencia!!'.format(2000 / 2))
    if b == 4:
        x = int(input('Em quantas vezes? '))
        z = 2000 / 5
        print('voce ira pagar pelo seu ps4 {}x de R${} obrigado pela preferencia!'.format(x, (2000 / x) + z / x))
if ex == 3:
    print('você escolheu o Iphone ')
    print('esse produto custa R$5000')
    print("Digite 1 para\n à vista no dinheiro/cheque 10% de desconto\ndigite 2 para"
          "\nà vista no cartão 5% de desconto\ndigite 3 para\nem 2x no cartão: preço normal"
          "\ndigite 4 para 3x ou mais no cartão com 20% de juros")
    b = int(input('Qual seria a forma de pagamento?'))
    if b == 1:
        print('você ira pagar pelo seu iphone R${} obrigado pela preferencia!!'.format(5000 - 5000 / 10))
    if b == 2:
        print('você ira pagar pelo seu iphone R${:.2f} obrigado pela preferencia!!'.format(5000 - 5000 / 20))
    if b == 3:
        print('você ira pagar pelo seu iphone 2x de R${} obrigado pela preferencia!!'.format(5000 / 2))
    if b == 4:
        x = int(input('Em quantas vezes? '))
        z = 5000 / 5
        print('voce ira pagar pelo seu iphone {}x de R${} obrigado pela preferencia!'.format(x, (5000 / x) + z / x))
