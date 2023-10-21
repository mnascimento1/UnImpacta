
carrinho_de_compras = input().split() 


if (carrinho_de_compras != []):

 
  for i in range(len(carrinho_de_compras)):
    carrinho_de_compras[i] = int(carrinho_de_compras[i])   

def adicionar(lista, item):
  lista.append(item)


def remover(lista, item):
  if (item in lista):
    lista.remove(item)
  else:
    print(f'código {item} não encontrado')

def exibir(lista):
  lista.sort()
  
  for i in range(len(lista)):
    if (i < len(lista) - 1):
      print(lista[i], end=' ')
    else:
      print(lista[i])

comando = input().split()

while comando[0] != 'encerrar':

  if (comando[0] == 'adicionar'):
    adicionar(carrinho_de_compras, int(comando[1]))
  elif (comando[0] == 'remover'):
    remover(carrinho_de_compras, int(comando[1]))
  else:
    exibir(carrinho_de_compras)

  comando = input().split()

exibir(carrinho_de_compras)
