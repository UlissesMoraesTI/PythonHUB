print('')
print('*******************************************************')

peso = float(input('* Informe seu peso kg:'))

altura = float(input('* Informe sua altura:'))

print('*******************************************************')
print('* Peso....: ' + str(peso) + ' kilos')
print('* Altura..: ' + str(altura) + ' metros')
print('*******************************************************')

altura_quadrado = altura**2 

imc = peso / (altura ** 2)

imc = round(imc, 2)

print('* Quadrado: ' + str(altura_quadrado) + ' potência')
print('* IMC.....: ' + str(imc))
print('*******************************************************')

if imc   <  18.5:
    imc_descricao = 'Baixo peso'
elif imc >= 18.5 and imc <= 24.9:
    imc_descricao = 'Peso normal'
elif imc >= 25   and imc <= 29.9:
    imc_descricao = 'Sobrepeso'
elif imc >= 30   and imc <= 34.9:
    imc_descricao = 'Obesidade grau I'
elif imc >= 35   and imc <= 39.9:
    imc_descricao = 'Obesidade grau II'
elif imc >  40:
    imc_descricao = 'Obesidade grau III (grave)'

print('* Parecer.: ' + imc_descricao)
print('*******************************************************')
print('* Menor que 18,5         - Baixo peso                 *')
print('*           18,5 – 24,9  - Peso normal                *')
print('*           25,0 – 29,9  - Sobrepeso                  *')
print('*           30,0 – 34,9  - Obesidade grau I           *')
print('*           35,0 – 39,9  - Obesidade grau II          *')
print('*           40,0 ou mais - Obesidade grau III (grave) *')
print('*******************************************************')

