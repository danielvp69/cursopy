empleados = [
    [1, "Pedro", "20797232", 2334, 1.5, 25, True, "Sueldo"],
    [1, "Ana", "20797232", 2331, 1.5, 25, True, "SAC"],
    [3, "Daniel", "20797232", 234, 1.5, 25, True, "SAC"],
    [3, "Rulo", "20797232", 134, 1.5, 25, True, "Sueldo"],
    [4, "Caru", "20797232", 5334, 1.5, 25, True, "Sueldo"],
    [5, "osvaldo", "20797232", 3334, 1.5, 25, True, "SAC"],
    [6, "Juan", "20797232", 6334, 1.5, 25, True, "Sueldo"],
    [7, "maby", "20797232", 824, 1.5, 25, True, "Sueldo"]
]


saldo_inicial = 500
mv_diarios = [0]*30  # Puedo llenar un array o inicilizar de esta forma
# print(mv_diarios)

mv_diarios[1] = saldo_inicial


for mov in empleados:
    diadelmes = mov[0]
    if mov[7] == "Sueldo":
        mv_diarios[diadelmes] = mv_diarios[diadelmes] + mov[3]
    elif mov[7] == "SAC":
        mv_diarios[diadelmes] = mv_diarios[diadelmes] - mov[3]


print(mv_diarios)
