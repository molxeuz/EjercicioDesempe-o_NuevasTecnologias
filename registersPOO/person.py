
class Persona:
    
    def __init__(self, id, nombre, apellido, correo, contrasena):
        
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena
    
    # Getter and Setter (id)

    @property 
    def id(self):
        return self._id
    
    @id.setter 
    def id(self, id):
        self._id = id
        
    # Getter and Setter (nombre)
        
    @property 
    def nombre(self):
        return self._nombre
    
    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre
        
    # Getter and Setter (apellido)
        
    @property 
    def apellido(self):
        return self._apellido
    
    @apellido.setter 
    def apellido(self, apellido):
        self._apellido = apellido      
        
    # Getter and Setter (correo)
        
    @property 
    def correo(self):
        return self._correo
    
    @correo.setter 
    def correo(self, correo):
        self._correo = correo       
        
    # Getter and Setter (contraseña)
        
    @property 
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter 
    def contrasena(self, contrasena):
        self._contrasena = contrasena         
        
    # Metodo para registrar
    
    def registrar(self):
        
        self._id = input("Indique el id: ")
        self._nombre = input("Indique su nombre: ")
        self._apellido = input("Indique su apellido: ")
        self._correo = input("Indique su correo: ")
        self._contrasena = input("Indique la contraseña: ")
        
    def ver_registro(self):
        
        print(f"\n Id: {self._id} \n Nombre: {self._nombre} \n Apellido {self._apellido} \n Correo: {self.correo} \n")
        
    