from nodoFreq import NodoFreq
from nodoSenal import NodoSenal


def agregar_al_final(nodo_inicial, dato, tiempo, amplitud):
    nuevo_nodo = NodoFreq(dato, tiempo, amplitud)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial


def agregar_al_inicio(nodo_inicial, dato, tiempo, amplitud):
    nuevo_nodo = NodoFreq(dato, tiempo, amplitud)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo


def obtener_cabeza(nodo_inicial):
    return nodo_inicial


def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal


def existe(nodo, busqueda):
    while nodo != None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False


def imprimir_lista(nodo):
    while nodo != None:
        print(f"[ {nodo.dato} ]", end="")
        nodo = nodo.siguiente


def main():
    lista = None
    lista = agregar_al_final(lista, 2, 1, 1)
    lista = agregar_al_final(lista, 3, 1, 2)
    lista = agregar_al_final(lista, 0, 1, 3)
    lista = agregar_al_final(lista, 4, 1, 4)
    print("Lista inicial")
    imprimir_lista(lista)


main()    




    