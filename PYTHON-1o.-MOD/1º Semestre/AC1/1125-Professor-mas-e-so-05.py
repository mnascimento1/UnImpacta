trabalhos = float(input())
prova = float(input())

media = (trabalhos + prova) / 2

if media >= 6:
    print('aprovado')
elif (media < 6 and trabalhos >= 2.00):
    print('talvez com a sub')
else:  
    print('reprovado')
