import xml.etree.ElementTree as ET
import graphviz as gv


tree = ET.parse('ejemploEntrada.xml')
root = tree.getroot()

cont = 0
cont2 = 0
cont3 = 0


print("Señales:")
print("..................................................")
for senal in root.findall('senal'):    
    print(f'(',cont2+1,')  ',root[cont2].get('nombre'))
    cont2 += 1
print("..................................................")
num = int(input("Ingrese el numero de la señal que desea procesar: "))
num -= 1    
print("")


# nombre = root[num].get('nombre')
# tiempo = root[num].get('t')
# Amplitud = root[num].get('A')
# print("------------------------------------------------------------")
# print("\033[1;34m"+"M. Frecuencia "+'\033[0;m', end="")
# print(f'| Nombre = {nombre}, tiempo = {tiempo}, Amplitud = {Amplitud}')
# print("------------------------------------------------------------")

# rango = int(tiempo) * int(Amplitud)
  
# for j in range(0, rango):
#     cont3 += 1
#     print(f"[  {root[num][j].text}  ]", end="")
#     if cont3 == int(Amplitud):            
#         print("")
#         cont3 = 0

# #print("")

# print("------------------------------------------------------------")
# print("\033[1;34m"+"M. Patrones "+'\033[0;m', end="")
# print(f'| Nombre = {nombre}, tiempo = {tiempo}, Amplitud = {Amplitud}')
# print("------------------------------------------------------------")

        
# for j in range(0, rango):
#     cont3 += 1
#     if root[num][j].text != "0":
#         print(f"[  1  ]", end="")
#     else:
#         print(f"[  0  ]", end="")
#     #print(f"[  {root[num][j].text}  ]", end="")
#     if cont3 == int(Amplitud):            
#         print("")
#         cont3 = 0

# print("")

