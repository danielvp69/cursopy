empleados = [
    ["Pedro", "20797232", 2334, 1.5, 25, True, "Sueldo"],
    ["Ana", "20797232", 2331, 1.5, 25, True, "SAC"],
    ["Daniel", "20797232", 234, 1.5, 25, True, "SAC"],
    ["Rulo", "20797232", 134, 1.5, 25, True, "Sueldo"],
    ["Caru", "20797232", 5334, 1.5, 25, True, "Sueldo"],
    ["osvaldo", "20797232", 3334, 1.5, 25, True, "SAC"],
    ["Juan", "20797232", 6334, 1.5, 25, True, "Sueldo"],
    ["maby", "20797232", 824, 1.5, 25, True, "Sueldo"]
]


# Magia

Sueldos = sum([s[2] for s in empleados if s[6] == "Sueldo"])
sac = sum([s[2] for s in empleados if s[6] == "SAC"])
# Sueldos = [s[2] for s in empleados if s[6] == "Sueldo"]

# Sueldos = empleados[1, 3]

print("Suma de sueldos pagados " + str(Sueldos) +
      " Suma de SAC pagados " + str(sac))
