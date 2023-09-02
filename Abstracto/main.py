import xml.etree.ElementTree as ET
from nodoFreq import NodoFreq
from nodoSenal import NodoSenal
from tkinter import filedialog


def cargar_archivo():

    ruta = filedialog.askopenfilename(title = "Open File", filetypes=(("XML files", "*.xml"),("all files", "*.*")))
    try:
        xml_file = open(ruta)        
       
    except Exception as err:
        print('Error al abrir el archivo:', err)
    finally:
        xml_file.close()

    tree = ET.parse(ruta)
    root = tree.getroot()

    t = root[0].attrib['t']
    A = root[0].attrib['A']        
    largo = int(t) * int(A)
    lista_senal = None
        
    # Recorriendo el árbol XML
    for i in range(0, largo):        
        lista_senal = agregar_al_final(lista_senal, root[0][i].text, 1, 1)
        
    print("\n")    
    print("lista_senal inicial")
    print("\033[1;34m"+"[ Inicio ]"+'\033[0;m', end = "") 
    imprimir_lista(lista_senal)
    print("\033[1;34m"+"[ ┴ ]"+'\033[0;m')
    print("\n")
        
    print("\033[1;32m"+"Datos cargados exitosamente"+'\033[0;m')
      

def agregar_lista_senales(nodo_inicial, nombre, tiempo, amplitud):
    nuevo_nodo = NodoSenal(nombre, tiempo, amplitud)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial


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


def obtener_nombre(nodo_inicial, nombre):
    while nodo_inicial != None:
        if nodo_inicial.dato == nombre:
            return nodo_inicial
        nodo_inicial = nodo_inicial.siguiente
    return None


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


def imprimir_lista_senales(nodo):    
    while nodo != None:
        print(f"[ {nodo.nombre} ]", end="")
        nodo = nodo.siguiente   


def imprimir_lista(nodo):    
    while nodo != None:
        print(f"[ {nodo.dato} ]", end="")
        nodo = nodo.siguiente
    

def main():
    lista_senales = None
    lista_senales = agregar_lista_senales(lista_senales, "Prueba 1", 5, 4)
    lista_senal = None
    lista_senal = agregar_al_final(lista_senal, 2, 1, 1)
    lista_senal = agregar_al_final(lista_senal, 3, 1, 2)
    lista_senal = agregar_al_final(lista_senal, 0, 1, 3)
    lista_senal = agregar_al_final(lista_senal, 4, 1, 4)
    lista_senal = agregar_al_final(lista_senal, 0, 2, 1)
    lista_senal = agregar_al_final(lista_senal, 0, 2, 2)
    lista_senal = agregar_al_final(lista_senal, 6, 2, 3)
    lista_senal = agregar_al_final(lista_senal, 3, 2, 4)


    print("")
    print("lista_senales")
    imprimir_lista_senales(lista_senales)
    print("\n")
    print("lista_senal inicial") 
    imprimir_lista(lista_senal)
    print("\n")
    
       


#main()    
cargar_archivo()    