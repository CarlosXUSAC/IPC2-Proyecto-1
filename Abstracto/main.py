import xml.etree.ElementTree as ET
from nodoFreq import NodoFreq
from tkinter import filedialog
import graphviz
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
    salto = int(A)            
    largo = int(t) * int(A)
    lista_senal = NodoFreq
    lista_senal_ent = NodoFreq
    lista_senal = None
    cont = 0
    cont2 = 0
    cont3 = 0

    
    print("\n")
    print("Señales:")
    print("..................................................")
    for senal in root.findall('senal'):    
        print(f'(',cont2+1,')  ',root[cont2].get('nombre'))
        cont2 += 1
    print("..................................................")
    num = int(input("Ingrese el numero de la señal que desea procesar: "))
    num -= 1    
    print("")

        
    # Recorriendo el árbol XML
    for i in range(0, largo):        
        lista_senal = agregar_al_final(lista_senal, root[num][i].text, root[num][i].attrib['t'], root[num][i].attrib['A'])
        lista_senal_ent = agregar_al_final(lista_senal_ent, int(root[num][i].text), root[num][i].attrib['t'], root[num][i].attrib['A'])
        
    print("\n")    
    print("lista_senal inicial")     
    imprimir_lista(lista_senal, salto)
    # print("\033[1;34m"+"[ ┴ ]"+'\033[0;m')
    # print("\n")
        
    print("\033[1;32m"+"Datos cargados exitosamente"+'\033[0;m')

    
    return root, lista_senal, lista_senal_ent, t, A


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


def existe(nodo, busqueda, t, A):            
    n = t*A-1
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


def imprimir_lista(nodo, salto):
    print("\033[1;34m"+"[ Inicio ]"+'\033[0;m', end = "")    
    cont = 1
    salto = salto    
    while nodo != None:
        print(f"[ {nodo.dato} ]", end="")
        nodo = nodo.siguiente
        if cont == salto:            
            print("\n",end="")
            cont = 0        
        cont = cont + 1
    print("\033[1;34m"+"[ ┴ ]"+'\033[0;m')
    print("\n")
        

def imprimir_patrones(nodo, salto):
    print("\033[1;34m"+"[ Inicio ]"+'\033[0;m', end = "")    
    cont = 1
    salto = salto    
    while nodo != None:
        if nodo.dato == "0":
            print(f"[ {0} ]", end="")
            nodo = nodo.siguiente
        else:
            print(f"[ {1} ]", end="")
            nodo = nodo.siguiente
        if cont == salto:            
            print("\n",end="")
            cont = 0        
        cont = cont + 1
    print("\033[1;34m"+"[ ┴ ]"+'\033[0;m')
    print("\n")
    

def regresar_lista(nodo_inicial):
    while nodo_inicial != None:
        nodo_inicial = nodo_inicial.siguiente
    
    return nodo_inicial


def procesar_archivo(lista_senal, lista_senal_ent, t, A):
    listaTemp = lista_senal
    listaEnt = lista_senal_ent
    tx = t
    Ax = A
    #imprimir_lista(listaTemp, A)
    #imprimir_lista(listaEnt, A)
    # print(t, A)
    listaRedu = NodoFreq
    listaRedu = None
    listaRedu2 = NodoFreq
    listaRedu2 = None   
    #listaTemp, listaEnt ,tx ,Ax= cargar_archivo()
    t = int(tx)
    A = int(Ax)        
    print("\n")    
    cont = existe(listaTemp, "0", t, A) 
    fin = 1    

    imprimir_patrones(listaTemp, A)
           

    listaEnt = listaEnt.siguiente
    comp1 = math.trunc(cont * pow(10, -(A*4-1)))     #pow(10, -16)    
    res1 = cont-(comp1 * pow(10, (A*4-1)))           #pow(10, 16)   


    for i in range(0, A):
            listaRedu = agregar_al_final(listaRedu, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente          
    
    
    comp2 = math.trunc(res1 * pow(10, -(A*3)))
    print(comp2)   #imprime el numero de veces que se repite el patron
    res2 = res1-(comp2 * pow(10, (A*3)))

    if comp1 == comp2:
        print("Son iguales")
        fin = 0  

        for i in range(0, A):
            listaRedu = agregar_al_final(listaRedu, listaRedu.dato+listaEnt.dato, listaRedu.tiempo+','+listaEnt.tiempo, listaRedu.amplitud+','+listaEnt.amplitud)            
            listaEnt = listaEnt.siguiente
            listaRedu = listaRedu.siguiente
    else:
        for i in range(0, A):
            listaRedu2 = agregar_al_final(listaRedu2, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente               
                    
    comp3 = math.trunc(res2 * pow(10, -(A*2)))
    #print(comp3)   #imprime el numero de veces que se repite el patron
    res3 = res2-(comp3 * pow(10, (A*2)))    

    if comp1 == comp3:
        print("Son iguales")
        fin = 0
        
        for i in range(0, A):            
            listaRedu = agregar_al_final(listaRedu, listaRedu.dato+listaEnt.dato, listaRedu.tiempo+','+listaEnt.tiempo, listaRedu.amplitud+','+listaEnt.amplitud)            
            listaEnt = listaEnt.siguiente
            listaRedu = listaRedu.siguiente
    else:
        for i in range(0, A):
            listaRedu2 = agregar_al_final(listaRedu2, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente           

    comp4 = math.trunc(res3 * pow(10, -(A)))
    #print(comp4)   #imprime el numero de veces que se repite el patron
    res4 = res3-(comp4 * pow(10, A))    

    if comp1 == comp4:
        print("Son iguales")
        fin = 0

        for i in range(0, A):            
            listaRedu = agregar_al_final(listaRedu, listaRedu.dato+listaEnt.dato, listaRedu.tiempo+','+listaEnt.tiempo, listaRedu.amplitud+','+listaEnt.amplitud)            
            listaEnt = listaEnt.siguiente
            listaRedu = listaRedu.siguiente
    else:
        for i in range(0, A):
            listaRedu2 = agregar_al_final(listaRedu2, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente           


    comp5 = math.trunc(res4 * pow(10, 0))
    #print(comp5)   #imprime el numero de veces que se repite el patron
    res5 = res4-(comp5 * pow(10, 0)) 

    if comp1 == comp5:
        print("Son iguales")
        fin = 0

        for i in range(0, A):            
            listaRedu = agregar_al_final(listaRedu, listaRedu.dato+listaEnt.dato, listaRedu.tiempo+','+listaEnt.tiempo, listaRedu.amplitud+','+listaEnt.amplitud)            
            listaEnt = listaEnt.siguiente
            listaRedu = listaRedu.siguiente
    else:
        for i in range(0, A):
            listaRedu2 = agregar_al_final(listaRedu2, listaEnt.dato, listaEnt.tiempo, listaEnt.amplitud)
            listaEnt = listaEnt.siguiente 

    if fin == 1:        
        print("No hay concidencias\n")
        listaRedu = listaTemp  

        

    print("lista_senal Reducida")
    imprimir_lista(listaRedu, A)
    print("\n")
    #imprimir_lista(listaRedu2)


def generar_grafica(root, t, A, sel):
    dot = graphviz.Digraph('Arbol', format='png')


    t = root[sel].attrib['t']
    A = root[sel].attrib['A']
    labelt = f't={t}' 
    labelA = f'A={A}'

    tint = int(t)
    print(tint)
    Aint = int(A)
    print(Aint)

    par = tint % 2
    print(par)

    dot.node('1', root[sel].attrib['nombre'])
    dot.node('2', labelt)  
    dot.node('3', labelA)
    dot.edge('1', f'2')
    dot.edge('1', f'3')

    for i in range(3, Aint+3):  # (3,7)
        dot.node(f'{2}{i}', root[sel][i-3].text)    
        dot.edge('1', f'{2}{i}')

    n = 0
    for j in range(3, tint+2):  # (3,7)
        for i in range(3, Aint+3):  #columnas
            dot.node(f'{j}{i}', root[sel][i+n+(tint-5)].text)        #[i+n+(tint-5)] impares  
            dot.edge(f'{j-1}{i}', f'{j}{i}')
        n += Aint    

    # Guardamos el grafo en un archivo
    dot.render('arbol_con_6_hijos', view=True)


def escribir_archivo():
    
    raiz = ET.Element("root")
    doc = ET.SubElement(raiz, "doc")

    nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
    nodo1.text = "Texto de nodo1"

    ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"

    arbol = ET.ElementTree(raiz)
    arbol.write("prueba4.xml")


def main(): 
    # Variables para almacenar datos del estudiante y archivo cargado
    nombre_estudiante = "Carlos Hugo Rios Mancilla"
    carnet = "9520488"
    curso = "Introducción a la Programación y Computación 2 sección 'A'"
    carera = "ingenieria en Ciencias y Sistemas"
    semestre = "4to Semestre"
    archivo_cargado = False
    datos_procesados = []

    while True:
        # Mostrar el menú
        print("\nMenú:")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Inicializar sistema")
        print("7. Salida")
    
        opcion = input("Seleccione una opción: ")
        
        
    
        if opcion == "1":
            # Opción 1: Cargar archivo
            root, lista_senal, lista_senal_ent, t, A = cargar_archivo()
            archivo_cargado = True  
            imprimir_lista(lista_senal_ent, A)          
    
        elif opcion == "2":
            # Opción 2: Procesar archivo
            if archivo_cargado:
                procesar_archivo(lista_senal, lista_senal_ent, t, A)
                print("Archivo procesado correctamente")
            else:
                print("Primero debe cargar un archivo.")
    
        elif opcion == "3":
            # Opción 3: Escribir archivo de salida
            escribir_archivo()
            #print(f"Archivo de salida '{nombre_salida}' generado correctamente")
            
    
        elif opcion == "4":
            # Opción 4: Mostrar datos del estudiante
            print("\n")
            print("...................................................................")
            print(f"Nombre del estudiante: {nombre_estudiante}")
            print(f"Carnet: {carnet}")
            print(f"Curso: {curso}")
            print(f"Carrera: {carera}")
            print(f"Semestre: {semestre}")
            print("...................................................................")
            print("\n")
    
        elif opcion == "5":
            # Opción 5: Generar gráfica
            cont = 0
            cont2 = 0
            cont3 = 0
            print("\n")
            print("Señales:")
            print("..................................................")
            for senal in root.findall('senal'):    
                print(f'(',cont2+1,')  ',root[cont2].get('nombre'))
                cont2 += 1
            print("..................................................")
            num = int(input("Ingrese el numero de la señal que desea procesar: "))
            num -= 1    
            print("")
            generar_grafica(root, t, A, num)
            print("Gráfica generada correctamente")
            
    
        elif opcion == "6":
            # Opción 6: Inicializar sistema
            lista_senal = None
            lista_senal_ent = None
            print("Sistema inicializado correctamente")
    
        elif opcion == "7":
            # Opción 7: Salida
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
main()