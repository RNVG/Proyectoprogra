import funcionesCrearU

empleados = {}
habitaciones = {}
huespeds = {}
reservaciones = {}
respaldos = {}

while True:
    print("---------------------------------------------------")
    print("-Bienvenido al sistema de gestión del hotel Universo-")
    print(" -Por favor seleccione la opción que desea emplear-")
    print("------------------------------------------------")
    print("----------------Menu Funciones------------------")
    print("------------------------------------------------")
    print("1. Personal")
    print("2. Reservas")
    print("3. Salir")
    opc = input("Seleccione una opción:")

    if (opc == "1"):
        print("Bienvenido al gestionamiento del personal")
        funcionesCrearU.crearU(empleados)

    elif (opc == "2"):
        print("Reservas")

    elif (opc == "3"):
        print("Gracias por visitar el programa")
        break  # Salir del bucle mientras True
