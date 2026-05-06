class Animal:
    def emitir_som(self):
        print("O animal esta emitindo um som...")

class Cachorro(Animal):       
    def emitir_som(self):
        print("O cachorro esta latindo...")

class Gato(Animal):          
    def emitir_som(self):
        print("O gato esta miando...")  

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()
