class Forma():
    def area(self):
        pass

class Quadrado(Forma):
    # Método Construtor
    # O método __init__ (Dander Init)
    # é o Método construtor da classe, 
    # que é chamado quando um objeto é criado a partir da classe. 
    # Ele recebe um parâmetro lado, que representa o comprimento do lado 
    # do quadrado, e atribui esse valor ao atributo self.lado.
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    #   return self.lado * self.lado            

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(f'Area do quadrado: {area_quadrado}')

quadrado2 = Quadrado(7)
area_quadrado2 = quadrado2.area()
print(f'Area do quadrado2: {area_quadrado2}')

circulo = Circulo(4)
area_circulo = circulo.area()
print(f'Area do circulo: {area_circulo}')

circulo2 = Circulo(6)
area_circulo2 = circulo2.area()
print(f'Area do circulo2: {area_circulo2}')