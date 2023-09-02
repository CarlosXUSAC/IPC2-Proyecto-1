import graphviz
import xml.etree.ElementTree as ET

# Amplitud Impar
    
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


tree = ET.parse('prueba2.xml')
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

par = tint % 2
print(par)

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
    for i in range(3, tint+1):
        dot.node(f'{j}{i}', root[0][i+n+(tint-5)].text)        #[i+n+(tint-5)] impares  
        dot.edge(f'{j-1}{i}', f'{j}{i}')
    n += Aint    




# Guardamos el grafo en un archivo
dot.render('arbol_con_6_hijos', view=True)