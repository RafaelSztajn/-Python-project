import random
import time
print('O que você deseja escolher?\n[1] PAPEL\n[2] TESOURA\n[3]PEDRA')
e = int(input('Escolha:'))
q = random.randint(1, 3)
# 1= papel
# 2=tesoura
# 3=pedra
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)
if e == q:
    print('empate')
    print('o computador escolheu o mesmo que você!!')
elif e == 1 and q == 2:
    print('o computador escolheu tesoura \n papel x tesoura= tesoura\n você perdeu!!')
elif e == 1 and q == 3:
    print('o computador escolheu pedra \npapel x pedra= papel\n Você ganhou!!')
elif e == 2 and q == 1:
    print('o computador escolheu papel \n tesoura x papel= tesoura\n você ganhou!!')
elif e == 2 and q == 3:
    print('o computador escolheu pedra \ntesoura x pedra= pedra\n você perdeu!! ')
elif e == 3 and q == 1:
    print('o computador escolheu papel \npedra x papel= papel\n você perdeu!!')
elif e == 3 and q == 2:
    print('o computador escolheu tesoura \npedra x tesoura= pedra\n você ganhou!! ')