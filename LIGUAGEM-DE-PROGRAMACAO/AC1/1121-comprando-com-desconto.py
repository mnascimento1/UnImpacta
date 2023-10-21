preco = float(input())
qtd = int(input())

valor = preco * qtd
desconto = ((0.1+(qtd*0.01))* valor)
total = valor - desconto

print(f'{valor:.2f}')
print(f'{total:.2f}')
