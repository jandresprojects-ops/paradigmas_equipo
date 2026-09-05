# Análisis Comparativo: Sistema de Gestión de Estudiantes
Este proyecto contiene la implementación de un **Sistema Básico de Gestión de Estudiantes** desarrollado bajo tres paradigmas de programación distintos (Estructurado, Funcional, Orientado POO ) utilizando Python como lenguaje de programacion.

# 1. Análisis Comparativo por Paradigma

1. **Programación Estructurada**
# Ventajas:
    - Simplicidad de lectura y rápida implementación.
    - Mínimo consumo de recursos.
    - Ideal para scripts o programas pequeños.
# Desventajas:
    - El uso de estado global dificulta el escalamiento.
    - Acoplamiento elevado a medida que crece el proyecto.
    - Mantenimiento complejo en sistemas grandes.
2. **Programación Orientada a Objetos (POO)**
# Ventajas:
    - Modelado cercano a entidades del mundo real.
    - Alta reutilización de código mediante herencia.
    - Encapsulamiento que asegura la integridad de los datos.
# Desventajas:
    - Mayor cantidad de código inicial y verbosidad.
    - Curva de diseño arquitectónico más compleja.
    - Ligera sobrecarga en rendimiento por instanciación de objetos.
3. **Programación Funcional**
# Ventajas:
    - Ausencia de efectos secundarios gracias al uso de funciones puras.
    - Facilidad para depurar y probar módulos independientes.
    - Inmutabilidad que previene errores de estado concurrente.
# Desventajas:
    - Curva de aprendizaje técnica más exigente.
    - Posible mayor consumo de memoria al crear nuevos estados inmutables.
    - Comprensión menos directa para programadores principiantes.

# 2. Conclusiones: ¿Cuándo usar cada paradigma?

**Programación Estructurada:** 
Recomendable para scripts de automatización, tareas secuenciales simples, prototipos rápidos o componentes donde la complejidad del dominio sea baja y no se requiera reutilización extensiva.

**Programación Orientada a Objetos (POO):** 
Ideal para aplicaciones empresariales, sistemas orientados a dominio donde interactúan entidades complejas con responsabilidades y comportamientos definidos (motores de videojuegos, interfaces gráficas).

**Programación Funcional:** 
para procesamiento masivo de datos (Big Data), sistemas concurrentes/-paralelos, desarrollo de microservicios y módulos financieros o científicos donde la integridad de los datos e inmutabilidad sean críticas.
