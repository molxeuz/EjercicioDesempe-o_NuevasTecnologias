
import os

def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiar_consola()

# --------------------

class Vehiculo:
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    
    def ver_vehiculo(self):
        print(f"\nMarca {self.marca} \nModelo: {self.modelo} \nColor: {self.color} \n")


vehiculo_1 = Vehiculo("Tesla", "Modelo X", "Negro")

if __name__ == '__main__':

    print(vehiculo_1.marca) # Tesla
    print(vehiculo_1.modelo) # Modelo X
    print(vehiculo_1.color) # Negro

    vehiculo_1.modelo = "Modelo Y"

    ver = vehiculo_1.ver_vehiculo() # Imprime todos los datos
