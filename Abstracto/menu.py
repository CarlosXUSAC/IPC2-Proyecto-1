# Variables para almacenar datos del estudiante y archivo cargado
nombre_estudiante = ""
archivo_cargado = False
datos_procesados = []

while True:
    # Mostrar el menú
    print("\nMenú:")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo de salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Inicializar sistema")
    print("7. Salida")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Opción 1: Cargar archivo
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        # Aquí puedes agregar código para cargar el archivo

        # Simulamos la carga del archivo
        archivo_cargado = True

    elif opcion == "2":
        # Opción 2: Procesar archivo
        if archivo_cargado:
            # Aquí puedes agregar código para procesar el archivo cargado
            print("Archivo procesado correctamente")
        else:
            print("Primero debe cargar un archivo.")

    elif opcion == "3":
        # Opción 3: Escribir archivo de salida
        if datos_procesados:
            nombre_salida = input("Ingrese el nombre del archivo de salida: ")
            # Aquí puedes agregar código para escribir los datos procesados en un archivo de salida
            print(f"Archivo de salida '{nombre_salida}' generado correctamente")
        else:
            print("No hay datos procesados para escribir.")

    elif opcion == "4":
        # Opción 4: Mostrar datos del estudiante
        print(f"Nombre del estudiante: {nombre_estudiante}")

    elif opcion == "5":
        # Opción 5: Generar gráfica
        if datos_procesados:
            # Aquí puedes agregar código para generar una gráfica
            print("Gráfica generada correctamente")
        else:
            print("No hay datos procesados para generar la gráfica.")

    elif opcion == "6":
        # Opción 6: Inicializar sistema
        nombre_estudiante = input("Ingrese su nombre: ")
        archivo_cargado = False
        datos_procesados = []
        print("Sistema inicializado correctamente")

    elif opcion == "7":
        # Opción 7: Salida
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
