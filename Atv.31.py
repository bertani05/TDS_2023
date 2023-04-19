a = float(input("Digite o valor de A:\n "))
print(50*'=')
b = float(input("Digite o valor de B:\n "))
print(50*'=')
c = float(input("Digite o valor de C:\n "))
print(50*'=')
if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triângulo.")
else:
    print("Os valores não formam um triângulo.")