import xml.etree.ElementTree as ET

tree = ET.parse('prueba.xml')
root = tree.getroot()


for elemento in root.findall('senal'):
    nombre = elemento.find('nombre')
    id_val = elemento.get('id')
    print(f"nombre: Nombre={nombre}, ID={id_val}")

    for item in elemento.findall('item'):
        value = item.get('value')
        text = item.text
        print(f"item: value={value}, text={text}")