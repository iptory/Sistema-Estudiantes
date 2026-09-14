def crear_estudiante(legajo, nombre, curso):
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "curso": curso,
        "notas": [],
        "materias": []
    }

    print("Estudiante cargado correctamente.")
    print("Legajo:", legajo)
    print("Nombre:", nombre)
    print("Curso:", curso)

    return estudiante


def listar_estudiantes(lista):
    if len(lista) == 0:
        print("No hay estudiantes cargados.")
        return

    for estudiante in lista:
        mostrar_diccionario(estudiante)
        print("--------------------")


def listar_nombres(lista):
    if len(lista) == 0:
        print("No hay estudiantes cargados.")
        return

    for i in range(len(lista)):
        print("ID:", i, "-", lista[i]["nombre"])


def mostrar_diccionario(dic):
    print("Legajo:", dic["legajo"])
    print("Nombre:", dic["nombre"])
    print("Curso:", dic["curso"])

    if len(dic["notas"]) == 0:
        print("Notas: no hay notas cargadas.")
    else:
        print("Notas:", dic["notas"])

    if len(dic["materias"]) == 0:
        print("Materias: no hay materias cargadas.")
    else:
        print("Materias:", dic["materias"])


def calcularPromedioLista(lista):
    if len(lista) == 0:
        print("No hay notas para calcular el promedio.")
        return 0

    suma = 0

    for numero in lista:
        suma = suma + numero

    promedio = suma / len(lista)
    return promedio
