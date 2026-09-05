# ============================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - GESTIÓN DE ESTUDIANTES
# Características: Encapsulamiento, Herencia, Polimorfismo,
# Abstracción e Instanciación de objetos.
# ============================================

from abc import ABC, abstractmethod

# ABSTRACCIÓN: Clase base abstracta que define el contrato general
class Persona(ABC):
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre.strip()  # Atributo protegido con limpieza de espacios
        self._edad = edad              # Atributo protegido

    @abstractmethod
    def obtener_informacion(self) -> str:
        """Método abstracto que obliga su implementación en clases hijas."""
        pass

# HERENCIA: Estudiante extiende las propiedades de Persona
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, calificaciones: list):
        super().__init__(nombre, edad)
        # ENCAPSULAMIENTO: Atributos privados controlados
        self.__calificaciones = calificaciones
        self.__promedio = self.__calcular_promedio()

    def __calcular_promedio(self) -> float:
        """Método privado auxiliar."""
        if not self.__calificaciones:
            return 0.0
        return sum(self.__calificaciones) / len(self.__calificaciones)

    # Getters para acceso seguro a miembros privados
    def get_nombre(self) -> str:
        return self._nombre

    def get_promedio(self) -> float:
        return self.__promedio

    # POLIMORFISMO: Implementación específica del método de la clase abstracta
    def obtener_informacion(self) -> str:
        return f"{self._nombre} | Edad: {self._edad} | Promedio: {self.__promedio:.2f}"

# CLASE GESTORA: Encapsula la colección de estudiantes y sus operaciones
class SistemaGestionEstudiantes:
    def __init__(self):
        self.__estudiantes = []  # Estado interno encapsulado

    def agregar_estudiante(self, estudiante: Estudiante):
        self.__estudiantes.append(estudiante)
        print(f"✅ [POO] Objeto Estudiante '{estudiante.get_nombre()}' guardado.")

    def buscar_estudiantes(self, nombre: str) -> list:
        """Retorna una lista con todos los objetos Estudiante que coincidan."""
        busqueda = nombre.strip().lower()
        coincidencias = []
        for est in self.__estudiantes:
            if busqueda in est.get_nombre().lower():
                coincidencias.append(est)
        return coincidencias

    def mostrar_estudiantes(self):
        if not self.__estudiantes:
            print("⚠️ No hay estudiantes registrados.")
            return
        
        print("\n--- LISTA DE ESTUDIANTES (POO) ---")
        for i, est in enumerate(self.__estudiantes, 1):
            print(f"{i}. {est.obtener_informacion()}")

def menu_principal():
    sistema = SistemaGestionEstudiantes()

    # INSTANCIACIÓN DE OBJETOS
    sistema.agregar_estudiante(Estudiante("Ana García", 20, [85, 90, 88, 92]))
    sistema.agregar_estudiante(Estudiante("Ana López", 22, [90, 91, 89, 94]))
    sistema.agregar_estudiante(Estudiante("Carlos López", 19, [78, 82, 85, 80]))
    sistema.agregar_estudiante(Estudiante("María Rodríguez", 21, [95, 98, 93, 97]))

    while True:
        print("\n" + "="*40)
        print(" SISTEMA POO - GESTIÓN DE ESTUDIANTES")
        print("="*40)
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Mostrar todos los estudiantes")
        print("4. Salir")
        
        opcion = input("\n👉 Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad: "))
            califs = []
            num_califs = int(input("Número de calificaciones: "))
            for i in range(num_califs):
                califs.append(float(input(f"Calificación {i+1}: ")))
            
            nuevo_estudiante = Estudiante(nombre, edad, califs)
            sistema.agregar_estudiante(nuevo_estudiante)
            
        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            resultados = sistema.buscar_estudiantes(nombre)
            if resultados:
                print(f"\n🔍 Se encontraron {len(resultados)} estudiante(s):")
                for est in resultados:
                    print(f"• {est.obtener_informacion()}")
            else:
                print("❌ No se encontraron estudiantes")
                
        elif opcion == '3':
            sistema.mostrar_estudiantes()
            
        elif opcion == '4':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu_principal()