import json
import os
from cliente import Cliente
from pila import Pila


def cargar_clientes(ruta):
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


def filtrar_urgentes(lista):
    filtrados = []
    i = 0
    while i < len(lista):
        persona = lista[i]
        if persona.tipo_cita == "Extraccion" and persona.prioridad == "Urgente":
            filtrados.append(persona)
        i = i + 1
    return filtrados


def ordenar_por_fecha(lista):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if lista[j].fecha < lista[j + 1].fecha:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
            j = j + 1
        i = i + 1
    return lista


def guardar_informe(pila, ruta):
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("INFORME DE PILA - CONSULTORIO ODONTOLOGICO\n")
    archivo.write("Clientes para extraccion dental con prioridad urgente\n")
    archivo.write("Orden: fecha mas cercana a la mas lejana (cima de la pila primero)\n")
    archivo.write("------------------------------------------------------------\n")
    orden = pila.listar_desde_cima()
    if len(orden) == 0:
        archivo.write("No hay clientes urgentes para extraccion.\n")
    else:
        numero = 1
        i = 0
        while i < len(orden):
            persona = orden[i]
            archivo.write(str(numero) + ". " + persona.mostrar() + "\n")
            numero = numero + 1
            i = i + 1
    archivo.close()


def main():
    print("CONSULTORIO ODONTOLOGICO - PLAN DE CONTINGENCIA")
    print("Pila de clientes con extraccion urgente")
    print("------------------------------------------------------------")

    clientes = cargar_clientes("datos/clientes.json")
    urgentes = filtrar_urgentes(clientes)
    urgentes = ordenar_por_fecha(urgentes)

    pila = Pila()
    i = 0
    while i < len(urgentes):
        pila.apilar(urgentes[i])
        i = i + 1

    print("Total de clientes cargados:", len(clientes))
    print("Clientes en la pila (extraccion + urgente):", pila.tamano())
    print("")
    print("Informe de llamada (de la cima hacia abajo):")
    print("")

    informe = pila.listar_desde_cima()
    if len(informe) == 0:
        print("No hay clientes para atender en la pila.")
    else:
        numero = 1
        i = 0
        while i < len(informe):
            print(str(numero) + ". " + informe[i].mostrar())
            numero = numero + 1
            i = i + 1

    print("")
    print("Atencion desde la pila (desapilar):")
    print("")
    orden_llamado = 1
    while pila.esta_vacia() == False:
        persona = pila.desapilar()
        print("Llamando " + str(orden_llamado) + ": " + persona.nombre + " - Fecha " + persona.fecha)
        orden_llamado = orden_llamado + 1

    if not os.path.exists("informes"):
        os.mkdir("informes")

    pila_informe = Pila()
    i = 0
    while i < len(urgentes):
        pila_informe.apilar(urgentes[i])
        i = i + 1
    guardar_informe(pila_informe, "informes/informe_pila.txt")
    print("")
    print("El informe se guardo en informes/informe_pila.txt")


if __name__ == "__main__":
    main()
