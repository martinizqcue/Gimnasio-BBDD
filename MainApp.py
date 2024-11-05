from GestorGimnasio import GestorGimnasio

def menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Listar clientes")
    print("4. Listar clientes morosos")
    print("5. Agregar aparato")
    print("6. Eliminar aparato")
    print("7. Listar aparatos")
    print("8. Agregar sesión")
    print("9. Listar sesiones por día")
    print("10. Eliminar sesión")
    print("11. Generar recibo")
    print("12. Listar recibos")
    print("13. Registrar pago")
    print("0. Salir")

if __name__ == "__main__":
    gestor = GestorGimnasio()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        # CRUD para clientes
        if opcion == "1":
            id_cliente = input("Ingrese ID del cliente: ")
            nombre = input("Ingrese nombre del cliente: ")
            gestor.agregar_cliente(id_cliente, nombre)

        elif opcion == "2":
            id_cliente = input("Ingrese ID del cliente a eliminar: ")
            gestor.eliminar_cliente(id_cliente)

        elif opcion == "3":
            clientes = gestor.listar_clientes()
            for cliente in clientes:
                print(cliente)

        elif opcion == "4":
            gestor.listar_morosos()

        # CRUD para aparatos
        elif opcion == "5":
            id_aparato = input("Ingrese ID del aparato: ")
            nombre = input("Ingrese nombre del aparato: ")
            gestor.agregar_aparato(id_aparato, nombre)

        elif opcion == "6":
            id_aparato = input("Ingrese ID del aparato a eliminar: ")
            gestor.eliminar_aparato(id_aparato)

        elif opcion == "7":
            aparatos = gestor.listar_aparatos()
            for aparato in aparatos:
                print(aparato)

        # CRUD para sesiones
        elif opcion == "8":
            id_sesion = input("Ingrese ID de la sesión: ")
            dia = input("Ingrese día de la sesión (lunes a viernes): ")
            hora = input("Ingrese hora de la sesión (formato 24h): ")
            id_cliente = input("Ingrese ID del cliente: ")
            id_aparato = input("Ingrese ID del aparato: ")
            gestor.agregar_sesion(id_sesion, dia, hora, id_cliente, id_aparato)

        elif opcion == "9":
            dia = input("Ingrese día para listar sesiones (lunes a viernes): ")
            sesiones = gestor.listar_sesiones()
            for sesion in sesiones:
                if sesion.dia == dia:
                    print(sesion)

        elif opcion == "10":
            id_sesion = input("Ingrese ID de la sesión a eliminar: ")
            gestor.eliminar_sesion(id_sesion)

        # CRUD para recibos
        elif opcion == "11":
            id_recibo = input("Ingrese ID del recibo: ")
            id_cliente = input("Ingrese ID del cliente: ")
            mes = input("Ingrese mes del (1-12): ")
            mensualidad = input("Ingrese mensualidad del recibo: ")
            gestor.generar_recibo(id_recibo, id_cliente, mes, mensualidad)

        elif opcion == "12":
            recibos = gestor.listar_recibos()
            for recibo in recibos:
                print(recibo)

        elif opcion == "13":
            id_cliente = input("Ingrese ID del cliente para registrar pago: ")
            gestor.registrar_pago(id_cliente)

        # Salida
        elif opcion == "0":
            print("Saliendo del programa...")
            break

        # Opción no válida
        else:
            print("Opción no válida, intente nuevamente.")

