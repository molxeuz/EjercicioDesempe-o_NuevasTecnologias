
from person import Persona

class Empleado(Persona):
    
    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario):
        
        super().__init__(id, nombre, apellido, correo, contrasena)
        
        self._cargo = cargo
        self._salario = salario
        
    # Getter and Setter (cargo)

    @property 
    def cargo(self):
        return self._cargo
    
    @cargo.setter 
    def cargo(self, cargo):
        self._cargo = cargo
        
    # Getter and Setter (salario)

    @property 
    def salario(self):
        return self._salario
    
    @salario.setter 
    def salario(self, salario):
        self._salario = salario
        
        
    def registrar(self):
        
        super().registrar()
        
        self.cargo = input("Ingrese el cargo: ")
        self.salario = float(input("Ingrese el salario: "))
        
    def ver_registro(self):
        
        super().ver_registro()
        
        print(f" Cargo: {self.cargo} \n Salario: {self.salario} \n")
        
    
    def iniciar_sesion(self):
        correo_reg = input("\n" + "Ingrese el correo registrado: ")
        contrasenas_reg = input("Ingrese la contraseña registrada: ")
        
        if correo_reg == self.correo and contrasenas_reg == self.contrasena:
            
            print(f"\n Bienvenido {self.nombre}!")
            return True
        
        else:
            
            print("Vaide sus credenciales")
            return False

    def iniciar_negocio_empleado(self, iniciar_sesion, ver_registro):
        
        init = iniciar_sesion()
        
        while init == True:
            
            print(" 1. Ver datos usuario \n 2. -------- \n 3.Salir")
            opcion = int(input("\n" + "Seleccione una opción: "))
            
            if opcion == 1:
                
                print("\n" + "Ver datos usuario \n")
                ver_registro()
                
            elif opcion == 2:
                
                print("\n" + "-------- \n")
                
            elif opcion == 3:
                
                print("\n" + "Saliendo....")
                int = False
        
            else: 
                print("Seleccione una opción correcta...")
