from time import sleep

saldo = int(input('Quanto de saldo voce tem? '))
casa = int(input('qual o valor da casa? '))              
print('''
[ 1 ] uma parcela
[ 2 ] duas parcelas
[ 3 ] três parcelas                     ''')
op = int(input('Quantas parcelas voce quer? '))

res1 = casa / 1
res2 = casa / 2
res3 = casa / 3

saldo2 = saldo / 1
saldo3 = saldo / 2
saldo4 = saldo / 3

falta = saldo - casa

#####Analise se seu saldo é compativel

if casa < saldo2 >= casa:
    print('Seu saldo é compativel com a compra')
elif saldo2 < casa:
    print('seu saldo não é compativel')
    print('Falta {} $ para seguir com a compra'.format(falta))
    exit()

elif saldo3 > casa:
    print('Seu saldo é compativel com a compra')
elif saldo3 < casa:
    print('seu saldo não é compativel')
    print('Falta {} $ para seguir com a compra'.format(falta))
    exit()

elif saldo4 > casa:
    print('seu saldo é compativel com a compra')
elif saldo4 < casa:
    print('Falta {} $ para seguir com a compra'.format(falta))
    exit()
#########################################

print('Proces.')
sleep(1)
print('processan..')
sleep(1)
print('processando...')


if op == 1:
    print('A parcela selecionada ficarar no valor de {}'.format(res1))
elif op == 2:
    print('A parcela selecionada ficarar no valor de {}'.format(res2))
elif op == 3:
    print('A parcela selecionada ficarar no valor de {}'.format(res3))

print('''
[ 1 ] Sim
[ 2 ] Não 
''')
cont = int(input('deseja continuar na compra? 1 Ou 2: '))

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
