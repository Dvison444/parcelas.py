from time import sleep

saldo = int(input('Quanto de saldo voce tem? '))
casa = int(input('qual o valor da casa? '))              
print('''
[ 1 ] uma parcela
[ 2 ] duas parcelas
[ 3 ] três parcelas                     ''')
op = int(input('Quantas parcelas voce quer? '))
res1 = saldo - casa
res2 = saldo - casa
res3 = saldo - casa


 
if __name__ == '__main__':
 
    delay = 5        # em segundos
 
    print('processando…')
    sleep(delay)
    print('')



if op == 1:
    print('A parcela selecionada ficarar no valor de {:.2f}'.format(res2))
elif op == 2:
    print('A parcela selecionada ficarar no valor de {:.2f}'.format(res2))
elif op == 3:
    print('A parcela selecionada ficarar no valor de {:.2f}'.format(res3))

print('''
[ 1 ] para sim
[ 2 ] para não
''')
cont = int(input('deseja continuar na compra? '))

if cont == 2:
    exit()

if op == res1:
    print('opção selecionada')


if saldo < casa:
    print('''
|XXXXXXXXXXXXXXXXXXXXXXXXX|    
|    compra invalida      |
|XXXXXXXXXXXXXXXXXXXXXXXXX|''')
elif saldo > casa:
    print('''
|=============================|   
|    compra bem sucedida      |
|=============================|   ''')

