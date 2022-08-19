

# Funciones anonimas lambda


#def multiplique(x, v): return x*v


#print(multiplique(5, 9))


def operacion(y, t):
    return y*t


def Miresultado(j, v): return operacion(j, v)


print(Miresultado(9, 78))


# Funcion Map

def al_cuadrado(x):
    return x*x


lis = [2, 34, 56, 4, 34, 3, 4, 344, ]

for i in map(al_cuadrado, lis):
    print(i)

# lo tengo en forma de lista

Otraformalista = list(map(al_cuadrado, lis))

print(Otraformalista)


# Filtas uno o mas valores de un conunto de valores

l = list(range(100))

print(l)


def es_par(c):
    return not c % 2


l_resto = list(filter(es_par, l))

print("Son pares--> " + str(l_resto))


l_resimpar = list(filter(lambda x: x % 2, l))

print("Son impares--> " + str(l_resimpar))
