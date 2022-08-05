
# Listas
numero = [3, 4, 6, 8, 2, 89]

print(numero[2])

empleados = ["pEDRO", "20797232", 2334, 1.5, 25, True]

nombre = empleados[0]
sueldo = empleados[2]


empleados[0] = "Daniel"
nombre = empleados[0]
print(nombre, sueldo)


# Tuplas. Estas no se pueden modificar una ves inicializadas

clientes = ("Samsonite", "20797232", 2334, 1.5, 25, True)

customer = clientes[0]

# clientes[0] = "Unisol" -- Da error pues no se puede modificar
print(customer)

# ---------------------------------------OPERCIONES----------

# Agregar
capacitaciones = ['Ventas', 'Java']
empleados.append(capacitaciones)

print(empleados)

# borradpo

# del empleados[1]

print(empleados)

# obtener partesd e la cadena subcadenas

subcadenaempleados = empleados[2:4]

print(subcadenaempleados)


otrosdatos = ["Rojo", "verde", "amarillo"]

print(empleados)

#empleados[2:] = otrosdatos
# print(empleados)


empleados[2:4] = otrosdatos
print(empleados)
