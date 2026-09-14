from funciones.gestor_estudiante import crear_estudiante
from funciones.gestor_estudiante import listar_estudiantes
from funciones.gestor_estudiante import listar_nombres
from funciones.gestor_estudiante import calcularPromedioLista


lista_bd = []
opcion = 0

while opcion != 7:
    print("\nSISTEMA DE GESTIÓN ESCOLAR")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Ingresar nota a un estudiante")
    print("4. Calcular promedio individual")
    print("5. Agregar una materia")
    print("6. Mostrar materias cursadas")
    print("7. Salir")

    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        legajo = len(lista_bd) + 10000
        nombre = input("Ingresá el nombre: ")
        curso = input("Ingresá el curso: ")

        estudiante = crear_estudiante(legajo, nombre, curso)
        lista_bd.append(estudiante)

    elif opcion == 2:
        listar_estudiantes(lista_bd)

    elif opcion == 3:
        listar_nombres(lista_bd)

        if len(lista_bd) > 0:
            id_estudiante = int(input("Ingresá el ID del estudiante: "))

            if id_estudiante >= 0 and id_estudiante < len(lista_bd):
                nota = int(input("Ingresá la nota: "))
                lista_bd[id_estudiante]["notas"].append(nota)
                print("Nota agregada correctamente.")
            else:
                print("Ese ID no existe.")

    elif opcion == 4:
        listar_nombres(lista_bd)

        if len(lista_bd) > 0:
            id_estudiante = int(input("Ingresá el ID del estudiante: "))

            if id_estudiante >= 0 and id_estudiante < len(lista_bd):
                notas = lista_bd[id_estudiante]["notas"]
                promedio = calcularPromedioLista(notas)
                print("El promedio es:", promedio)
            else:
                print("Ese ID no existe.")

    elif opcion == 5:
        listar_nombres(lista_bd)

        if len(lista_bd) > 0:
            id_estudiante = int(input("Ingresá el ID del estudiante: "))

            if id_estudiante >= 0 and id_estudiante < len(lista_bd):
                materia = input("Ingresá el nombre de la materia: ")
                lista_bd[id_estudiante]["materias"].append(materia)
                print("Materia agregada correctamente.")
            else:
                print("Ese ID no existe.")

    elif opcion == 6:
        listar_nombres(lista_bd)

        if len(lista_bd) > 0:
            id_estudiante = int(input("Ingresá el ID del estudiante: "))

            if id_estudiante >= 0 and id_estudiante < len(lista_bd):
                materias = lista_bd[id_estudiante]["materias"]

                if len(materias) == 0:
                    print("Este estudiante no tiene materias cargadas.")
                else:
                    print("Materias cursadas:")
                    for materia in materias:
                        print("-", materia)
            else:
                print("Ese ID no existe.")

    elif opcion == 7:
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")
