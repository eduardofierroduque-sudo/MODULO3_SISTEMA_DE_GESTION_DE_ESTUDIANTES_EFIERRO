# 1. Crear una lista de estudiantes
# Usamos la lista base proporcionada en el punto 9
estudiantes = ["Juan", "Ana", "Pedro", "Laura", "Luis"]

# Agregamos un nuevo estudiante usando el método adecuado (.append)
estudiantes.append("Marta")

# 2. Modificar la lista de estudiantes
# Cambiamos el tercer estudiante (índice 2, ya que Python empieza en 0)
estudiantes[2] = "Roberto"

# 3 y 4. Crear tuplas de calificaciones y asociarlas en un diccionario
# La estructura de la tupla es (asignatura1, asignatura2, asignatura3)
calificaciones = {
    "Juan": (85, 90, 78),
    "Ana": (92, 88, 95),
    "Roberto": (70, 75, 80),
    "Laura": (88, 82, 91),
    "Luis": (60, 65, 70),
    "Marta": (95, 98, 92)
}

# Imprimir las calificaciones de un estudiante a elección
estudiante_elegido = "Ana"
print(f"Calificaciones de {estudiante_elegido}: {calificaciones[estudiante_elegido]}")

# 5. Uso de conjuntos (Sets)
asignaturas = {"Matemáticas", "Física", "Historia", "Programación", "Química"}

# Agregar una asignatura adicional y eliminar una
asignaturas.add("Arte")
asignaturas.discard("Química")

# 6. Operación entre conjuntos
asignaturas_optativas = {"Música", "Teatro", "Fotografía"}

# Realizar la unión de los dos conjuntos
todas_las_asignaturas = asignaturas.union(asignaturas_optativas)
print(f"\nUnión de todas las asignaturas: {todas_las_asignaturas}")

# 7. Comprobaciones y salidas
# Comprobar si un estudiante específico está en la lista
print(f"\n¿Está 'Juan' en la lista?: {'Juan' in estudiantes}")

# Verificar si una asignatura está en el conjunto
print(f"¿Está 'Física' en el conjunto de asignaturas?: {'Física' in asignaturas}")

# 8. Impresión final
print("\n--- RESULTADOS FINALES ---")
print(f"Lista de estudiantes: {estudiantes}")
print(f"Diccionario de calificaciones: {calificaciones}")
print(f"Conjunto final de asignaturas: {asignaturas}")