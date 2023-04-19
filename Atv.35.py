n1 = input('Digite 1 para Álcool e 2 para Gasolina?\n')
print(50*'=')
n2 = float(input('Digite quantos litros de combustível?\n'))
print(50*'=')
if n1 == '1':
    if n2 <= 20:
        v = n2 * 2.9
        v = v - v * 0.03
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
    else:
        v = n2 * 2.9
        v = v - v * 0.05
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
elif n1 == '2':
    if n2 <= 20:
        v = n2 * 3.3
        v = v - v * 0.04
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
    else:
        v = n2 * 3.3
        v = v - v * 0.06
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
else:
    print('Tente Novamente...')
