import xml.etree.ElementTree as ET


try:
    xml_file = open('prueba2.xml')

    if xml_file.readable():        
        xml_data = ET.fromstring(xml_file.read())

        lst_senal = xml_data.findall('senal')
        print(f"Total de señales: {len(lst_senal)}")
        for senal in lst_senal:
            nodo1 = lst_senal.getElementByTagName('senal')[0]
            print(f"nombre: {senal.firstChild.data}")
            print("--------------------------------------------------")

    else:
        print(False)    

except Exception as err:
    print('Error al abrir el archivo:', err)
finally:
    xml_file.close()
