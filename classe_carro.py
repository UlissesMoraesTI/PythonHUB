class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print("O carro esta acelerando...")

    def frear(self):
        print("O carro esta freiando...")   

    def buzinar(self):
        print("O carro esta buzinando...")

carro = Carro()        

carro.acelerar()
carro.frear()
carro.buzinar()
    
class Uno(Carro):
    marca = 'Fiat'
    modelo = 'Uno'
    cor = 'Vermelho'
    ano = 2020

uno = Uno()

print(f'Marca: {Uno.marca}')
print(f'Modelo: {Uno.modelo}')
print(f'Cor: {Uno.cor}')
print(f'Ano: {Uno.ano}')
print(f'Numero de rodas: {Uno.numero_rodas}')
print(f'Quantidade de passageiros: {Uno.quantidade_passageiros}')

uno.acelerar()
uno.frear()
uno.buzinar()
