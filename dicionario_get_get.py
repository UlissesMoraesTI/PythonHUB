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


