n1 = input('Digite 1 para Morango e 2 para Maçã ?\n')
print(50 * '=')

n2 = float(input('Digite quantos Kg de frutas?\n'))
print(50 * '=')

if n1 == '1':
    if n2 <= 5:
        v = n2 * 2.5
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
    else:
        v = n2 * 2.2
        v = round(v, 2)

elif n1 == '2':
    if n2 <= 5:
        v = n2 * 1.8
        v = round(v, 2)
        print(f'O valor total a pagar R${v}')
    else:
        v = n2 * 1.5
        v = round(v, 2)

