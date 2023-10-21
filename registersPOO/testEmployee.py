
from employee import Empleado

empleado_1 = Empleado(id=None, nombre=None, apellido=None, correo=None, contrasena=None, cargo=None, salario=None)

empleado_1.registrar()
# empleado_1.ver_registro()
empleado_1.iniciar_negocio_empleado(empleado_1.iniciar_sesion(), empleado_1.ver_registro())