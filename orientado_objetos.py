# ============================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - GESTIÓN DE ESTUDIANTES
# Características: Encapsulamiento, Herencia, Polimorfismo,
# Abstracción e Instanciación de objetos.
# ============================================

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre.strip()  
        self._edad = edad              

    @abstractmethod
    def obtener_informacion(self) -> str:
        pass

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, calificaciones: list, rfc: str = '', curp: str = '', numero_telefonico: str = ''):
        super().__init__(nombre, edad)
        self.__rfc = rfc.strip().upper()
        self.__curp = curp.strip().upper()
        self.__numero_telefonico = numero_telefonico.strip()
        self.__calificaciones = calificaciones
        self.__promedio = self.__calcular_promedio()

    def __calcular_promedio(self) -> float:
        if not self.__calificaciones:
            return 0.0
        return sum(self.__calificaciones) / len(self.__calificaciones)

    def get_nombre(self) -> str:
        return self._nombre

    def get_promedio(self) -> float:
        return self.__promedio

    def get_rfc(self) -> str:
        return self.__rfc

    def get_curp(self) -> str:
        return self.__curp

    def get_numero_telefonico(self) -> str:
        return self.__numero_telefonico

    def obtener_informacion(self) -> str:
        return f"{self._nombre} | Edad: {self._edad} | RFC: {self.__rfc} | CURP: {self.__curp} | Teléfono: {self.__numero_telefonico} | Promedio: {self.__promedio:.2f}"

class SistemaGestionEstudiantes:
    def __init__(self):
        self.__estudiantes = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.__estudiantes.append(estudiante)
        print(f" [POO] Objeto Estudiante '{estudiante.get_nombre()}' guardado.")

    def buscar_estudiantes(self, nombre: str) -> list:
        busqueda = nombre.strip().lower()
        coincidencias = []
        for est in self.__estudiantes:
            if busqueda in est.get_nombre().lower():
                coincidencias.append(est)
        return coincidencias

    def mostrar_estudiantes(self):
        if not self.__estudiantes:
            print("No hay estudiantes registrados.")
            return
        
        print("\n--- LISTA DE ESTUDIANTES ---")
        for i, est in enumerate(self.__estudiantes, 1):
            print(f"{i}. {est.obtener_informacion()}")

def menu_principal():
    sistema = SistemaGestionEstudiantes()

    sistema.agregar_estudiante(Estudiante("Artemio Rangel", 20, [85, 90, 88, 92], "GARA000000AAA", "GARA000000MDFNNNA0", "8972174187"))
    sistema.agregar_estudiante(Estudiante("Josue Andres", 22, [90, 91, 89, 94], "LOPA000000AAA", "LOPA000000MDFPNNA0", "8952352357"))
    sistema.agregar_estudiante(Estudiante("Yael Grageda", 19, [78, 82, 85, 80], "LOPC000000AAA", "LOPC000000HDFPNRA0", "8972080907"))

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
            while True:
                try:
                    edad = int(input("Edad: "))
                    break
                except ValueError:
                    print("Ingrese la edad correctamente.")
            rfc = input("RFC: ")
            curp = input("CURP: ")
            numero_telefonico = input("Número de teléfono personal: ")
            califs = []
            num_califs = int(input("Número de calificaciones: "))
            for i in range(num_califs):
                califs.append(float(input(f"Calificación {i+1}: ")))
            
            nuevo_estudiante = Estudiante(nombre, edad, califs, rfc, curp, numero_telefonico)
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