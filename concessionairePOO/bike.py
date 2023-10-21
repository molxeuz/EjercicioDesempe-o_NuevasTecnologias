
import os

def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiar_consola()

# --------------------

from vehicle import Vehiculo

class Moto(Vehiculo):
    
    freno = "abs"

    def __init__(self, marca, modelo, color, categoria):
        super().__init__(marca, modelo, color)
        self.categoria = categoria
        
    def ver_vehiculo(self):
        super(Moto, self).ver_vehiculo()
        print(f"Categoria: {self.categoria} \nTipo freno: {self.freno} \n")
        
mt09 = Moto("Yamaha", "2023", "Negro mate", "Scooter")

mt09.ver_vehiculo()

    
