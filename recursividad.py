def cuentahaciaatras(n):
    if n == 0:
        print(n)
    else:
        print(n)
        cuentahaciaatras(n-1)


# cuentahaciaatras(50)


# Ordenamiento de listas usando recursividad

lista = [52, 87, 344, -98, 54, 78, 115, 7874, 1, 3]

print(lista)


def orden(lista):
    pivot = lista[0]
   # print(pivot)
    if len(lista) == 1:
        return[pivot]
    else:
        izq = [n for n in lista if n < pivot]
        izq_ordenanda = orden(izq) if len(izq) > 0 else []

        derecha = [n for n in lista if n > pivot]
        der_ordenada = orden(derecha) if len(derecha) > 0 else []
        return izq_ordenanda + [pivot] + der_ordenada


lista_ordenada = orden(lista)
print(lista_ordenada)
