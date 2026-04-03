pessoa = {
    'nome': 'Ulisses',
    'idade': 25,
    'profissao': 'Analista',
    'tecnologia': ['Cobol', 'Python', 'Java', 'React'],
    'formacao': ['Bacharel Sistemas de Informação', 'Dados', 'Front End React'],
    'pet': {
        'nome': 'Sol',
        'idade': 4,
        'peso': '3kg'
        }
    }

print(pessoa.get('nome'))
print(pessoa.get('tecnologia'))

print(' ')
print('--- Saída via GET ---')
print(pessoa.get('tecnologia')[0])
print(pessoa.get('tecnologia')[1])
print(pessoa.get('tecnologia')[2])
print(pessoa.get('tecnologia')[3])
print(' ')
print('--- Saída via [] ---')
print(pessoa['tecnologia'][0])
print(pessoa['tecnologia'][1])
print(pessoa['tecnologia'][2])
print(pessoa['tecnologia'][3])

print(' ')
print('--- Saída via for ---')

lista = pessoa['tecnologia']

i = 0

for linguagem in lista:
    i = i + 1
    print(i, linguagem)

print(' ')
print('--- Cadastro do Sol via .get ---')
print('--------------------------------')
print(pessoa.get('pet'))
print(pessoa.get('pet').get('nome'))
print(pessoa.get('pet').get('idade'))
print(pessoa.get('pet').get('peso'))

print(' ')
print('--- Cadastro do Sol via [] ---')
print('------------------------------')
print(pessoa['pet'])
print(pessoa['pet']['nome'])
print(pessoa['pet']['idade'])
print(pessoa['pet']['peso'])


