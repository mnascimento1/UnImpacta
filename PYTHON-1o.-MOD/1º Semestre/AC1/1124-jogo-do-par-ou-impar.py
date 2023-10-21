numero = int(input())

if numero % 2 == 0:
    impar = numero - 1
    par = numero + 2
else:
    impar = numero - 2
    par = numero + 1

print(f'{impar} {par}')
