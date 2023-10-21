import sys, os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_consola()

empleados = []
colillas_pago = []

calcular_salario_neto_lambda = lambda salario, salario_minimo: salario + 140000 if salario < 2 * salario_minimo else salario

usuarios_registrados = {}

def registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    tipo_usuario = input("Ingrese el tipo de usuario (analista o empleado): ")

    if nombre_usuario in usuarios_registrados:
        print("El usuario ya existe. Ingrese otro nombre de usuario.")
    else:
        usuarios_registrados[nombre_usuario] = {"contraseña": contraseña, "tipo": tipo_usuario}
        print("Usuario registrado con éxito.")
        # Llamar la función de inicio de sesión después del registro
        iniciar_sesion(nombre_usuario)

def iniciar_sesion(nombre_usuario):
    contraseña = input("Contraseña: ")
    limpiar_consola()

    if nombre_usuario in usuarios_registrados and usuarios_registrados[nombre_usuario]["contraseña"] == contraseña:
        tipo_usuario = usuarios_registrados[nombre_usuario]["tipo"]
        print(f"\nInicio de sesión exitoso como {tipo_usuario}.\n")
        if tipo_usuario == "analista":
            analista()
        elif tipo_usuario == "empleado":
            empleado()
    else:
        print("\nError: Nombre de usuario o contraseña incorrectos.\n")

def agregar_empleado(id, nombre, apellido, cargo, area, salario):
    empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "area": area,
        "salario": salario
    }
    empleados.append(empleado)

def listar_empleados():
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}")

def calcular_salario_neto():
    salario_minimo = 1160000
    for empleado in empleados:
        salario_neto = calcular_salario_neto_lambda(empleado['salario'], salario_minimo)
        empleado['salario_neto'] = salario_neto
        colillas_pago.append((empleado, salario_neto))

def imprimir_colilla_pago():
    for empleado, salario_neto in colillas_pago:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Salario Neto: {salario_neto}")

def buscar_empleado_por_id(id):
    for empleado in empleados:
        if empleado['id'] == id:
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Salario Neto: {empleado['salario_neto']}")
            return
    print("Empleado no encontrado")

def registrar_empleado():
    id = int(input("Ingrese el ID del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    area = input("Ingrese el área del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    limpiar_consola()
    agregar_empleado(id, nombre, apellido, cargo, area, salario)
    print(f"Empleado {nombre} {apellido} registrado con éxito.")
    after_action_callback()

def menu_listar_empleados():
    print("\nEmpleados:")
    listar_empleados()
    after_action_callback()

def menu_calcular_salarios():
    calcular_salario_neto()
    print("\nSalarios netos calculados.")
    after_action_callback()

def menu_imprimir_colillas():
    print("\nColillas de Pago:")
    imprimir_colilla_pago()
    after_action_callback()

def menu_buscar_empleado():
    id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
    buscar_empleado_por_id(id_buscado)
    after_action_callback()

def analista():
    while True:
        print("\nMenú:")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Calcular salarios netos")
        print("4. Imprimir colillas de pago")
        print("5. Buscar empleado por ID")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            menu_listar_empleados()
        elif opcion == "3":
            menu_calcular_salarios()
        elif opcion == "4":
            menu_imprimir_colillas()
        elif opcion == "5":
            menu_buscar_empleado()
        elif opcion == "6":
            login()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def empleado():
    while True:
        print("\n MENU ")
        print("1. Buscar colilla de pago con tu cédula")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            calcular_salario_neto()
            id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
            buscar_empleado_por_id(id_buscado)
            after_action_callback()
        elif opcion == "2":
            login()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def login():
    print("\n INICIO DE SESIÓN ")
    print("                                    ")
    print("1. Iniciar sesión                   ")
    print("2. Registrar usuario                ")
    print("3. Salir                            ")

    print("                                    ")

    modo = input("Ingrese el modo deseado: ")

    if modo == "1":
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        limpiar_consola()
        
        if nombre_usuario not in usuarios_registrados:
            print("Usuario no registrado. Registre un usuario primero.")
            login()
        elif usuarios_registrados[nombre_usuario]["contraseña"] != contraseña:
            print("Contraseña incorrecta.")
            login()
        else:
            iniciar_sesion(nombre_usuario)
    elif modo == "2":
        registrar_usuario()
    elif modo == "3":
        print("\nSaliendo del programa.")
        sys.exit()
    else:
        print("\nOpción no válida. Por favor, seleccione una opción válida.")

def after_action_callback():
    input("\nPresiona Enter para continuar...")
    limpiar_consola()

login()