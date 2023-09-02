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

# Crea un objeto de grafo
dot = graphviz.Digraph(comment='Grafo Vertical', format='png')

# Llama a la función para crear el grafo vertical
create_vertical_graph(root, dot)

# Renderiza el grafo en un archivo de imagen
dot.render('grafo_vertical', view=True)
