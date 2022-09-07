class cliente:
    """ tipode cliente de la empresa"""

    def __init__(self, Nombre, apellido, domicilio, localidad, fechanac, tipo, zona, estrellas=None, VentasMensuales=None, premios=None):
        self.nombre = Nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.localidad = localidad
        self.fechanac = fechanac
        self.tipo = tipo
        self.zona = zona
        self.estrellas = estrellas if estrellas is not None else "0"
        self.VentasMensuales = VentasMensuales if VentasMensuales is not None else []
        self.premios = premios if premios is not None else []

    def _str_(self):
        return self.nombre

    def agregapremio(self, Listapremios):
        self.premios.append(Listapremios)


class ClienteExclusivo(cliente):

    def revx(self, hotel):
        print('Hotal del exlcvivo ' + hotel)


class Listapremios:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __repr__(self) -> str:
        return "Premio <{},{}>".format(self.id, self.nombre)


class TipoRev:
    """ tipode cliente de la empresa"""

    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo


class Zonarev:
    """ zona cliente"""

    def __init__(self, id, nombre, localidad):
        self.id = id
        self.nombre = nombre
        self.localidad = localidad

    def __str__(self):
        return self.localidad

    def _repr_(self):
        return self.localidad


zona1 = Zonarev(1, "Lujas 1", "Tandil")

"""cliente1 = cliente("Daniel", "Penachi", "oncativo 1959",
                   "CABA", "09/0/1969", "X", "658")"""


premio1 = Listapremios(1, "Cafetera")
premio2 = Listapremios(2, "Matera")
premio3 = Listapremios(3, "Pulidora")
premio4 = Listapremios(4, "Secadora")

"""
cliente1.agregapremio(premio2)
cliente1.agregapremio(premio1)
cliente1.agregapremio(premio4)
"""

"""cliente_Exclusivo_1 = ClienteExclusivo("Pedro", "Perez", "oncativo 1959", "CABA", "09/0/1969", "X", "658", "3232", "ggg")




***print(cliente_Exclusivo_1)***"""

cliente2 = ClienteExclusivo(
    "Daniel", "Penachi", "Carlos calvo", "caba", "02/02/02", "x", "656", "222")

Hotel = cliente2.revx("Majisterio")

cliente2.agregapremio(premio3)
cliente2.agregapremio(premio1)

print(Hotel)
"""
"""
print(cliente2.premios)
