import graphviz
import xml.etree.ElementTree as ET


def create_vertical_graph(root, graph):
    cont = 0
    if 'nombre' in root.attrib:
        node_name = root.attrib['nombre']
        graph.node(node_name)
        for dato in root.findall('dato'):
            cont += 1
            #t = dato.attrib['t']
            #A = dato.attrib['A']
            texto = dato.text
            label = f'{texto}'
            graph.node(label)
            graph.edge(node_name, label)
            node_name = label
            if cont == 4:
                break


# Parsea el archivo XML
tree = ET.parse('testChat.xml')
root = tree.getroot()

# Creamos un objeto Digraph
dot = graphviz.Digraph('Arbol', format='png')

# Agregamos nodos al grafo
dot.node('1', 'Raíz')

# Agregamos 6 hijos a la raíz
for i in range(1, 7):
    dot.node(f'{2}{i}', f'Hijo {i}')
    print(f'{2}{i}')
    dot.edge('1', f'{2}{i}')

r = 0
for i in range(3, 4):
    for j in range(3, 7):   # La cantidad de hijos que tiene cada nodo
        dot.node(f'{j}{i}', f'Hijo {i+r+4}')
        dot.edge(f'{j-1}{i}', f'{j}{i}')
        dot.node(f'{j}{i+1}', f'Hijo {i+r+5}')
        dot.edge(f'{j-1}{i+1}', f'{j}{i+1}')
        dot.node(f'{j}{i+2}', f'Hijo {i+r+6}')
        dot.edge(f'{j-1}{i+2}', f'{j}{i+2}')
        dot.node(f'{j}{i+3}', f'Hijo {i+r+7}')
        dot.edge(f'{j-1}{i+3}', f'{j}{i+3}')
        r += 3


# dot.node(f'C3', f'Hijo 7')
# dot.edge('B3', f'C3')
# dot.node(f'C4', f'Hijo 8')
# dot.edge('B4', f'C4')
# dot.node(f'C5', f'Hijo 9')  
# dot.edge('B5', f'C5')
# dot.node(f'C6', f'Hijo 10')
# dot.edge('B6', f'C6')

# dot.node(f'D3', f'Hijo 11')
# dot.edge('C3', f'D3')
# dot.node(f'D4', f'Hijo 12')
# dot.edge('C4', f'D4')
# dot.node(f'D5', f'Hijo 13')
# dot.edge('C5', f'D5')
# dot.node(f'D6', f'Hijo 14')
# dot.edge('C6', f'D6')

# dot.node(f'E3', f'Hijo 15')
# dot.edge('D3', f'E3')
# dot.node(f'E4', f'Hijo 16')
# dot.edge('D4', f'E4')
# dot.node(f'E5', f'Hijo 17')
# dot.edge('D5', f'E5')
# dot.node(f'E6', f'Hijo 18')
# dot.edge('D6', f'E6')



# Guardamos el grafo en un archivo
dot.render('arbol_con_6_hijos', view=True)
