class Celular:
    marca = 'Samsung'
    modelo = 'Galaxy S21'
    cor = 'Preto'
    camera = '108MP'
    memoria = '128GB'
    bateria = '4000mAh'

    def fazer_ligacao(self):
        print('Fazendo ligacao...')

    def jogar_jogo(self):
        print('Jogando jogo...')

    def despertador(self):
        print('Despertador ativado...')

    def calcular(self, num1, num2):
        resultado = num1 + num2
        print(f'O resultado da soma e: {resultado}')

celular = Celular()

print(f'Marca: {celular.marca}')
print(f'Modelo: {celular.modelo}')  
print(f'Cor: {celular.cor}')
print(f'Camera: {celular.camera}')
print(f'Memoria: {celular.memoria}')
print(f'Bateria: {celular.bateria}')

celular.fazer_ligacao()
celular.jogar_jogo()
celular.despertador()
celular.calcular(10, 20)
