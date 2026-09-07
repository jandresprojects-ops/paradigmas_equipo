# ============================================
# PROGRAMACIÓN ESTRUCTURADA - GESTIÓN DE ESTUDIANTES
# Características: Estado mutable centralizado, funciones modulares
# y flujo de control secuencial con variables globales/locales
# ============================================

estudiantes = []

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def agregar_estudiante(nombre, edad, calificaciones, rfc='', curp='', numeroTelefonico=''):
    global estudiantes
    estudiante = {
        'nombre': nombre.strip(),
        'edad': edad,
        'rfc': rfc.strip().upper(),
        'curp': curp.strip().upper(),
        'numeroTelefonico': numeroTelefonico.strip(),
        'calificaciones': calificaciones,
        'promedio': calcular_promedio(calificaciones)
    }
    estudiantes.append(estudiante)
    print(f"[Estructurado] Estudiante {nombre.strip()} agregado exitosamente.")

def buscar_estudiantes(nombre):
    busqueda = nombre.strip().lower()
    coincidencias = []
    for estudiante in estudiantes:
        if busqueda in estudiante['nombre'].lower():
            coincidencias.append(estudiante)
    return coincidencias

def dar_formato_estudiante(est):
    return f"{est['nombre']} | Edad: {est['edad']} | RFC: {est['rfc']} | CURP: {est['curp']} | Teléfono: {est['numeroTelefonico']} | Promedio: {est['promedio']:.2f}"

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n--- LISTA DE ESTUDIANTES (Estructurado) ---")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {dar_formato_estudiante(est)}")

def menu_principal():
    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("="*40)
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Mostrar todos los estudiantes")
        print("4. Salir")
        
        opcion = input("\n Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            while True:
                try:
                    edad = int(input("Edad: "))
                    break
                except ValueError:
                    print("Ingrese la edad correctamente.")
            
            rfc = input("RFC: ")
            curp = input("CURP: ")
            numeroTelefonico = input("Número de teléfono Personal: ")
            
            califs = []
            num_califs = int(input("Número de calificaciones: "))
            for i in range(num_califs):
                calif = float(input(f"Calificación {i+1}: "))
                califs.append(calif)
                
            agregar_estudiante(nombre, edad, califs, rfc, curp, numeroTelefonico)
            
        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            resultados = buscar_estudiantes(nombre)
            if resultados:
                print(f"\n🔍 Se encontraron {len(resultados)} estudiante(s):")
                for est in resultados:
                    print(f"• {dar_formato_estudiante(est)}")
            else:
                print(" No se encontraron estudiantes")
                
        elif opcion == '3':
            mostrar_estudiantes()
            
        elif opcion == '4':
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida")

if __name__ == "__main__":
    agregar_estudiante("Artemio Rangel", 20, [85, 90, 88, 92], "GARA000000AAA", "GARA000000MDFNNNA0", "8972174187")
    agregar_estudiante("Josue Andres", 22, [90, 91, 89, 94], "LOPA000000AAA", "LOPA000000MDFPNNA0", "8952352357")
    agregar_estudiante("Yael Grageda", 19, [78, 82, 85, 80], "LOPC000000AAA", "LOPC000000HDFPNRA0", "8972080907")
    
    menu_principal()