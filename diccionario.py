from importlib.abc import SourceLoader
from tkinter import commondialog


dic = [{"Codigo": "014452144", "Nombre": "Pedro aznar", "Domicilio": "Santo domingo 253314", "Sueldo": "11"},
       {"Codigo": "21445344", "Nombre": "Carls aznar",
           "Domicilio": "Santo salud 3", "Sueldo": "121"},
       {"Codigo": "414454552144", "Nombre": "Daniel aznar",
           "Domicilio": "Santo carlos 14", "Sueldo": "1352541"},
       {"Codigo": "214452144", "Nombre": "Jose aznar",
           "Domicilio": " domingo 314", "Sueldo": "141"},
       {"Codigo": "452144", "Nombre": "juana aznar",
           "Domicilio": " Martes 3313", "Sueldo": "151"}
       ]


dic1 = {"Codigo": "014452144", "Nombre": "Pedro aznar",
        "Domicilio": "Santo domingo 253314", "Sueldo": "11"}

cod = dic1["Codigo"]

print(cod)

dic1["Codigo"] = "AAAA"


cod = dic1["Codigo"]

print(cod)

dic1["Edad"] = "34"

edadd = dic1["Edad"]
print(edadd)

# Algunas funciones
# Si busco una clave y no existe el interprete me daria error para traerla es mas seguro asi

mascota = dic1.get("mascota", "No tiene mascota esta muerta")

print(mascota)

# Puedo tambien preguntar

existe_mascota = "mascota" in dic1

print(existe_mascota)

# Obtener un arreglo de las claves de un diccinario

claves = dic1.keys()

# print(claves)
print(claves)


# obtengo valores

valores = dic1.values()

print(valores)

# Poniendo los datos del diccinario en un arreglo

datos_puros = []

for d in dic:
    codigo_d = d.get("Codigo", "Sin codigo")
    nombre_d = d.get("Nombre", "Sin nombre")
    domicilio_d = d.get("Domicilio", "Sin doc")
    Sueldo_d = d.get("Sueldo", "Sin sueldo")
    datos_puros.append([codigo_d, nombre_d, domicilio_d, Sueldo_d])


print(datos_puros)
