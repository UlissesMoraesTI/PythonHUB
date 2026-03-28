valor_pago      = float(input('Valor Pago.....: r$ '))
valor_investido = float(input('Valor Investido: r$ '))
valor_venda     = float(input('Valor da Venda.: r$ ')) 

custo_total     = valor_pago  + valor_investido
lucro_total     = valor_venda - custo_total 

print ('----------------------------')
print ('Custo Total....: r$ ' + str(custo_total))

print (' ')
print ('----------------------------')
print ('Lucro na Venda.: r$ ' + str(lucro_total))

print (' ')
print ('----------------------------')

if lucro_total > 0:
    print ('Resultado Venda: Lucro r$ ' + str(lucro_total))
elif lucro_total < 0:
    print ('Resultado Venda: Prejuízo r$ ' + str(lucro_total))
else:    
    print ('Resultado Venda: Sem Lucro r$ ' + str(lucro_total))
    
    
    

