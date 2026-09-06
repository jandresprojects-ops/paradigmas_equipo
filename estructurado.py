# ============================================
# PROGRAMACIÓN ESTRUCTURADA - GESTIÓN DE ESTUDIANTES
# Características: Estado mutable centralizado, funciones modulares
# y flujo de control secuencial con variables globales/locales
# ============================================

# Variable global para almacenar el estado
estudiantes = []

def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones."""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def agregar_estudiante(nombre, edad, calificaciones):
    """Agrega un estudiante modificando el estado de la variable global."""
    global estudiantes
    estudiante = {
        'nombre': nombre.strip(),
        'edad': edad,
        'calificaciones': calificaciones,
        'promedio': calcular_promedio(calificaciones)
    }
    estudiantes.append(estudiante)
    print(f"[Estructurado] Estudiante {nombre.strip()} agregado exitosamente.")

def buscar_estudiantes(nombre):
    """Retorna una lista con todos los estudiantes que coincidan con la búsqueda."""
    busqueda = nombre.strip().lower()
    coincidencias = []
    for estudiante in estudiantes:
        if busqueda in estudiante['nombre'].lower():
            coincidencias.append(estudiante)
    return coincidencias

def mostrar_estudiantes():
    """Muestra los registros leídos de la variable global."""
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n--- LISTA DE ESTUDIANTES (Estructurado) ---")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']} | Edad: {est['edad']} | Promedio: {est['promedio']:.2f}")

def menu_principal():
    """Interfaz de consola interactiva."""
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
            califs = []
            num_califs = int(input("Número de calificaciones: "))
            for i in range(num_califs):
                calif = float(input(f"Calificación {i+1}: "))
                califs.append(calif)
            agregar_estudiante(nombre, edad, califs)
            
        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            resultados = buscar_estudiantes(nombre)
            if resultados:
                print(f"\n🔍 Se encontraron {len(resultados)} estudiante(s):")
                for est in resultados:
                    print(f"• Nombre: {est['nombre']} | Edad: {est['edad']} | Promedio: {est['promedio']:.2f}")
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
    # Carga de datos iniciales
    agregar_estudiante("Ana García", 20, [85, 90, 88, 92])
    agregar_estudiante("Ana López", 22, [90, 91, 89, 94])
    agregar_estudiante("Carlos", 19, [78, 82, 85, 80])
    agregar_estudiante("María Rodríguez", 21, [95, 98, 93, 97])
    
    menu_principal()