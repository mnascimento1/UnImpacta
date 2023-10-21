doacao = 0
n = float(input())
while n!= -1.0:
    doacao += n
    n = float(input())

print(f'VC$ {doacao:.2f}')
print(f'R$ {doacao * 2.50:.2f}')
 
