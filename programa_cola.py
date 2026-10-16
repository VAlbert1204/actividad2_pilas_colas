import json
import os
from cliente import Cliente
from cola import Cola


def cargar_agenda(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    lista = []
    i = 0
    while i < len(datos):
        registro = datos[i]
        persona = Cliente(
            registro["nombre"],
            registro["documento"],
            registro["telefono"],
            registro["tipo_cita"],
            registro["prioridad"],
            registro["fecha"],
            registro["hora"]
        )
        lista.append(persona)
        i = i + 1
    return lista


def guardar_informe(atendidos, ruta):
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("INFORME DE COLA - CONSULTORIO ODONTOLOGICO\n")
    archivo.write("Agenda del dia atendida en orden de llegada\n")
    archivo.write("------------------------------------------------------------\n")
    if len(atendidos) == 0:
        archivo.write("No se atendieron clientes.\n")
    else:
        numero = 1
        i = 0
        while i < len(atendidos):
            persona = atendidos[i]
            archivo.write(str(numero) + ". " + persona.mostrar() + "\n")
            numero = numero + 1
            i = i + 1
    archivo.close()


def main():
    print("CONSULTORIO ODONTOLOGICO - AGENDA DIARIA")
    print("Cola de atencion segun el orden de la agenda")
    print("------------------------------------------------------------")

    agenda = cargar_agenda("datos/agenda.json")
    cola = Cola()

    i = 0
    while i < len(agenda):
        cola.encolar(agenda[i])
        i = i + 1

    print("Clientes en cola:", cola.tamano())
    print("")
    print("Orden de la agenda (frente de la cola primero):")
    print("")

    lista = cola.listar()
    numero = 1
    i = 0
    while i < len(lista):
        print(str(numero) + ". " + lista[i].mostrar())
        numero = numero + 1
        i = i + 1

    print("")
    print("Atencion de clientes (desencolar):")
    print("")

    atendidos = []
    turno = 1
    while cola.esta_vacia() == False:
        persona = cola.desencolar()
        print("Atendiendo turno " + str(turno) + ": " + persona.nombre + " - Hora " + persona.hora)
        atendidos.append(persona)
        turno = turno + 1

    if not os.path.exists("informes"):
        os.mkdir("informes")

    guardar_informe(atendidos, "informes/informe_cola.txt")
    print("")
    print("El informe se guardo en informes/informe_cola.txt")


if __name__ == "__main__":
    main()
