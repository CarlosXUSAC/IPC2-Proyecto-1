import graphviz
import xml.etree.ElementTree as ET

# Amplitud Par
    
try:
    xml_file = open('prueba.xml', 'r')
    #print(xml_file.read()) # Imprime el contenido del archivo XML
    if xml_file.readable():
        #xml_data = ET.fromstring(xml_file.read()) # Parsea el archivo XML con read y lo guarda en xml_data
        xml_data = ET.fromstring(xml_file.read())
        lst_senales = xml_data.findall('senal')
        #print(xml_data) # Imprime el contenido del archivo XML
        print(len(lst_senales))   
            
    else:
        print(False)
except Exception as err:
    print(err)


tree = ET.parse('nery.xml')
root = tree.getroot()

dot = graphviz.Digraph('Arbol', format='png')


t = root[0].attrib['t']
A = root[0].attrib['A']
labelt = f't={t}' 
labelA = f'A={A}'

tint = int(t)
print(tint)
Aint = int(A)
print(Aint)

dot.node('1', root[0].attrib['nombre'])
dot.node('2', labelt)  
dot.node('3', labelA)
dot.edge('1', f'2')
dot.edge('1', f'3')

for i in range(3, Aint+3):  # (3,7)
    dot.node(f'{2}{i}', root[0][i-3].text)    
    dot.edge('1', f'{2}{i}')

n = 0
for j in range(3, tint+2):  # (3,7)
    for i in range(3, tint+2):
        dot.node(f'{j}{i}', root[0][i+n+(tint-4)].text)        #[i+n+(tint-4)] pares
        dot.edge(f'{j-1}{i}', f'{j}{i}')
    n += Aint    


# for i in range(3, 7):
#     dot.node(f'{3}{i}', root[0][i+1].text)
#     print(f'{3}{i}')
#     dot.edge(f'{2}{i}', f'{3}{i}')

# for i in range(3, 7):
#     dot.node(f'{4}{i}', root[0][i+5].text)
#     print(f'{4}{i}')
#     dot.edge(f'{3}{i}', f'{4}{i}')

    

# print(root[0].attrib['nombre'])
# print(root[1].attrib['nombre'])
# print(root[0][0].text)

# print(root[0][0].attrib['t'])
# print(root[0][0].attrib['A'])


# Guardamos el grafo en un archivo
dot.render('arbol_con_6_hijos', view=True)
