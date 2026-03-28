prova_1 = float(input('Prova 1.....: '))
prova_2 = float(input('Prova 2.....: '))
prova_3 = float(input('Prova 3.....: '))

media  = (prova_1 + prova_2 + prova_3) / 3

media = round(media, 2)

print (' ')
print ('----------------------------')
print ('Média final: ' + str(media))
print ('----------------------------')

if media >= 7:
    print ('Aprovado')
elif media < 5:
    print ('Reprovado')
else:    
    print ('Recuperação')

print ('----------------------------')
    

    
    
    
