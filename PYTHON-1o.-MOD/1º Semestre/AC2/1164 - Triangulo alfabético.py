n = int(input())
cont = 1
unicode = 65

while (n < 1 or n > 26):
  n = int(input())

while cont <= 26 and unicode <= 90: 
  print(f'{cont * chr(unicode)}')
  cont += 1
  unicode += 1
  if cont == (n + 1)
