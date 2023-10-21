
from person import Persona

persona_1 = Persona(id=None, nombre=None, apellido=None, correo=None, contrasena=None)

persona_1.id = "1"

print(persona_1.id)

persona_1.registrar()
persona_1.ver_registro()
