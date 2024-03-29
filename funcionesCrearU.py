def crearU(empleados):
    print("Funcion Creación de usuario")
    print("---------------------------")
    while True:
        try:
            cedula = int(input("Introduzca su numero de cédula:"))
            if cedula:
                break
        except ValueError:
            print("Ingrese correctamente su cédula")

    while True:
        try:
            nombre = input("Ingrese el nombre del usuario:")
            if nombre:
                break
        except ValueError:
            print("Ingrese correctamente el nombre del usuario:")

    while True:
        try:
            direccion = input("Ingrese su dirección:")
            if direccion:
                break
        except ValueError:
            print("Ingrese correctamente su dirección")

    while True:
        try:
            telefono = int(input("Ingrese su numero de telefono:"))
            if telefono:
                break
        except ValueError:
            print("Ingrese correctamente su numero de telefono: ")


    if cedula and nombre and direccion and telefono:
        empleados[cedula] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono
        }
        print("Se han guardado los datos personales del empleado")
    else:
        print("Por favor verifique que todos los espacios posean información correcta.")

    while True: #Hicimos este otro menu con la intención de facilitarnos el acesso a las opciones dependiendo el puesto elegido
        print("----------------------------------------")
        print("--------        PUESTOS       ----------")
        print("----------------------------------------")
        print("--1. Administrador         ----")
        print("--2. Recepcionista         ----")
        print("--3. Salir                 ----")
        print("Seleccione una opción")
        opc2 = int(input("--->"))

        if opc2 == 1:
            while True:
                usuario = input("Ingrese el nombre de usuario que desee:")
                if usuario:
                    break
                else:
                    print("Ingrese usuario válido")
            while True:
                contraseña = input("Introduzca la contraseña que desee:")
                if contraseña:
                    break
                else:
                    print("Contraseña no válida")

        elif opc2 == 2:
            while True:
                usuario = input("Ingrese el nombre de usuario que desee:")
                if usuario:
                    break
                else:
                    print("Ingrese usuario válido")
            while True:
                contraseña = input("ntroduzca la contraseña que desee:")
                if contraseña:
                    break
                else:
                    print("Ingrese contraseña válida")

        elif opc2 == 3:
            break  #Aqui le indicamos al ciclo que salga

        else:
            print("Opción no válida")










