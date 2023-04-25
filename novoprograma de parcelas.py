saldo = int(input('Quanto de saldo voce tem? '))
casa = int(input('qual o valor da casa? '))              
print('''
[ 1 ] uma parcela
[ 2 ] duas parcelas
[ 3 ] três parcelas                     ''')
op = int(input('Quantas parcelas voce quer?'))
res1 = (saldo + casa) / 1
res2 = (saldo + casa) / 2
res3 = (saldo + casa) / 3
if op == res1:
    print('opção selecionada')
if saldo < casa:
    print('compra invalida')
elif saldo > casa:
    print('compra bem sucedida')