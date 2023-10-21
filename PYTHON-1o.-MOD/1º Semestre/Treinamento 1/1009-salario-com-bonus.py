nome = input()
salario = float(input())
venda = float(input())

comissao = (venda * 0.15) + salario

print(f'TOTAL = R$ {comissao:.2f}')
