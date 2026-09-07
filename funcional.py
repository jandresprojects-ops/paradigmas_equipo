# ============================================
# PROGRAMACIÓN FUNCIONAL - GESTIÓN DE ESTUDIANTES
# Características: Inmutabilidad de estructuras, Funciones Puras,
# Funciones de Alto Orden (map, filter, reduce) y Expresiones Lambda.
# ============================================

from functools import reduce

# FUNCIONES PURAS: Mismas entradas producen siempre la misma salida sin alterar variables externas

def calcular_promedio(calificaciones: list) -> float:
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def crear_estudiante(nombre: str, edad: int, calificaciones: list, rfc: str = '', curp: str = '', numeroTelefonico: str = '') -> dict:
    return {
        'nombre': nombre.strip(),
        'edad': edad,
        'rfc': rfc.strip().upper(),
        'curp': curp.strip().upper(),
        'numeroTelefonico': numeroTelefonico.strip(),
        'calificaciones': tuple(calificaciones),
        'promedio': calcular_promedio(calificaciones)
    }

def agregar_estudiante(db_actual: tuple, nuevo_estudiante: dict) -> tuple:
    return db_actual + (nuevo_estudiante,)

def buscar_estudiantes(db_actual: tuple, nombre: str) -> list:
    busqueda = nombre.strip().lower()
    return list(filter(lambda est: busqueda in est['nombre'].lower(), db_actual))

def calcular_promedio_general(db_actual: tuple) -> float:
    if not db_actual:
        return 0.0
    promedios = list(map(lambda est: est['promedio'], db_actual))
    suma_total = reduce(lambda acc, p: acc + p, promedios, 0.0)
    return suma_total / len(promedios)

def dar_formato_estudiante(est: dict) -> str:
    return f"{est['nombre']} | Edad: {est['edad']} | RFC: {est['rfc']} | CURP: {est['curp']} | Teléfono: {est['numeroTelefonico']} | Promedio: {est['promedio']:.2f}"

def menu_principal():
    # Estructura de datos inmutable (Tupla) que representa el estado
    base_datos = ()

    # Carga de datos funcional (cada llamada genera un nuevo estado)
    base_datos = agregar_estudiante(base_datos, crear_estudiante("Artemio Rangel", 20, [85, 90, 88, 92], "GARA000000AAA", "GARA000000MDFNNNA0", "8972174187"))
    base_datos = agregar_estudiante(base_datos, crear_estudiante("Josue Andres", 22, [90, 91, 89, 94], "LOPA000000AAA", "LOPA000000MDFPNNA0", "8952352357"))
    base_datos = agregar_estudiante(base_datos, crear_estudiante("Yael Grageda", 19, [78, 82, 85, 80], "LOPC000000AAA", "LOPC000000HDFPNRA0", "8972080907"))
    

    while True:
        print("\n" + "="*40)
        print(" SISTEMA FUNCIONAL - GESTIÓN DE ESTUDIANTES")
        print("="*40)
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Mostrar todos los estudiantes (y promedio general)")
        print("4. Salir")
        
        opcion = input("\n Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad: "))
            rfc = input("RFC: ")
            curp = input("CURP: ")
            numeroTelefonico = input("Número de teléfono Personal: ")
            num_califs = int(input("Número de calificaciones: "))
            califs = [float(input(f"Calificación {i+1}: ")) for i in range(num_califs)]
            
            nuevo = crear_estudiante(nombre, edad, califs, rfc, curp, numeroTelefonico)
            base_datos = agregar_estudiante(base_datos, nuevo)
            print(" [Funcional] Registro procesado e integrado al nuevo estado.")
            
        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            resultados = buscar_estudiantes(base_datos, nombre)
            if resultados:
                print(f"\n Se encontraron {len(resultados)} estudiante(s):")
                # Aplicamos formato a cada resultado mapeando la función
                lineas = map(dar_formato_estudiante, resultados)
                print("\n".join(f"• {linea}" for linea in lineas))
            else:
                print(" No se encontraron estudiantes")
                
        elif opcion == '3':
            if not base_datos:
                print(" No hay estudiantes registrados.")
            else:
                print("\n--- LISTA DE ESTUDIANTES (Funcional) ---")
                lineas = [f"{i}. {dar_formato_estudiante(est)}" for i, est in enumerate(base_datos, 1)]
                print("\n".join(lineas))
                
                prom_gral = calcular_promedio_general(base_datos)
                print(f"\n Promedio General del Grupo: {prom_gral:.2f}")
                
        elif opcion == '4':
            print("By By")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()