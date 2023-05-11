def obtener_lista_csv(nombre_archivo):
    separador = ","
    with open(nombre_archivo, encoding="utf-8") as archivo:
        dbz_lista_pj = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columna = linea.split(separador)
            id_pj = columna[0]
            nombre = columna[1]
            raza = columna[2]
            poder_pelea = columna[3]
            poder_ataque = columna[4]
            habilidades =columna[5]
            dbz_lista_pj.append({
                "id" : int(id_pj),
                "nombre" : nombre,
                "raza" : raza,
                "poder_pelea" : int(poder_pelea),
                "poder_ataque" : int(poder_ataque),
                "habilidades" : habilidades,
            })
        return dbz_lista_pj
