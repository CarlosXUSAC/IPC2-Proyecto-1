import xml.etree.ElementTree as ET
from nodoFreq import NodoFreq
from nodoRed import NodoRed
from tkinter import filedialog
import math


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
    lista_senal = NodoFreq
    lista_senal_ent = NodoFreq
    lista_senal = None
        
    # Recorriendo el árbol XML
    for i in range(0, largo):        
        lista_senal = agregar_al_final(lista_senal, root[0][i].text, root[0][i].attrib['t'], root[0][i].attrib['A'])
        lista_senal_ent = agregar_al_final(lista_senal_ent, int(root[0][i].text), root[0][i].attrib['t'], root[0][i].attrib['A'])
        
    print("\n")    
    print("lista_senal inicial")
    print("\033[1;34m"+"[ Inicio ]"+'\033[0;m', end = "") 
    imprimir_lista(lista_senal)
    print("\033[1;34m"+"[ ┴ ]"+'\033[0;m')
    print("\n")
        
    print("\033[1;32m"+"Datos cargados exitosamente"+'\033[0;m')

    
    return lista_senal, lista_senal_ent

    
      

def agregar_lista_ent(nodo_inicial, dato, orden):
    nuevo_nodo = NodoRed(dato)
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
    n = 19
    cont = 0
    #nodo = nodo.siguiente
    while nodo != None:
        if nodo.dato != busqueda:            
            cont = cont + pow(10, n)            
            n = n-1        
        else:            
            n = n-1
        nodo = nodo.siguiente                  
    return cont



def imprimir_lista_ent(nodo):    
    while nodo != None:
        print(f"[ {nodo.dato} ]", end="")
        nodo = nodo.siguiente   


def imprimir_lista(nodo):    
    while nodo != None:
        print(f"[ {nodo.dato} ]", end="")
        nodo = nodo.siguiente
    

def regresar_lista(nodo_inicial):
    while nodo_inicial != None:
        nodo_inicial = nodo_inicial.siguiente
    
    return nodo_inicial


def avanzar(nodo_inicial, pasos):
    for i in range(0, pasos):
        nodo_inicial = nodo_inicial.siguiente
    return nodo_inicial


def main(): 
    listaRedu = NodoFreq
    listaRedu = None
    listaRedu2 = NodoFreq
    listaRedu2 = None   
    listaTemp, listaEnt = cargar_archivo()        
    print("\n")    
    cont = existe(listaTemp, "0")       
    

    listaEnt = listaEnt.siguiente
    comp1 = math.trunc(cont * pow(10, -16))
    print(comp1)
    res1 = cont-(comp1 * pow(10, 16))

    for i in range(0, 4):
            listaRedu = agregar_al_final(listaRedu, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente          

    rep = 0
    for i in range(0, 4):
        res2, comp2, listaRedu, listaRedu2 = reducir(listaEnt, listaRedu, listaRedu2, res1, comp1, 12-4*i, rep)
        avanzar(listaEnt, 4)
        avanzar(listaRedu, 4)
        rep =+ 1
        res1 = res2
        comp1 = comp2

     

        
    imprimir_lista(listaRedu)
    print("\n")
    imprimir_lista(listaRedu2)



def reducir(listaEnt, listaRedu,listaRedu2,res1,comp1,pot,rep):

    avanzar(listaEnt, rep)
    avanzar(listaRedu, rep)
       
    comp2 = math.trunc(res1 * pow(10, -pot))
    print(comp2)
    res2 = res1-(comp2 * pow(10, pot))    

    #print(comp1, comp2)
    if comp1 == comp2:
        print("Son iguales")       
        for i in range(0, 4):
            listaRedu = agregar_al_final(listaRedu, listaRedu.dato+listaEnt.dato, listaRedu.tiempo+','+listaEnt.tiempo, listaRedu.amplitud+','+listaEnt.amplitud)            
            listaEnt = listaEnt.siguiente
            listaRedu = listaRedu.siguiente
    else:
        for i in range(0, 4):
            listaRedu2 = agregar_al_final(listaRedu2, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente  

    return res2, comp2, listaRedu2, listaRedu                                         
  

main()      