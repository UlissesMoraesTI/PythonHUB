numeros = [1, 2, 3, 4, 5]

numeros_dobrados = [numero * 2 for numero in numeros]

print(numeros_dobrados)


nomes = ['Ana', 'Felipe', 'João', 'Arlindo', 'Carlos']

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos) 


nomes = ['Ana', 'Felipe', 'João', 'Arlindo', 'Carlos']

nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'A']

print(nomes_maiusculos) 
