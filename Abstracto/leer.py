from xml.dom import minidom

ruta = 'prueba.xml'
xmldoc = minidom.parse('prueba.xml')
print(xmldoc.toxml())
doc = xmldoc.getElementsByTagName('senal')

for doc in doc:
    print(doc.firstChild.data)
    print("--------------------------------------------------")