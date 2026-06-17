def eleccionAnyo():
    lista = [2013,2018,2021,2022,2023,2024]
    print("Elige el año para analizar:\n1. 2013\n2. 2018\n3. 2021\n4. 2022\n5. 2023\n6. 2024")
    return lista[int(input())-1]

def rangoEdad():
    lista = ['From 16 to 19 years', 'From 16 to 24 years','From 16 to 29 years', 'From 20 to 24 years','From 25 to 29 years', 'From 25 to 34 years','From 30 to 64 years', 'From 35 to 49 years','From 50 to 64 years', 'From 65 to 74 years', '16 years or over','65 years or over', '75 years or over']
    print("Elige un rango de Edades para analizar:\n1. From 16 to 19 years\n2. From 16 to 24 years\n3. From 16 to 29 years\n4. From 20 to 24 years\n5. From 25 to 29 years\n6. From 25 to 34 years\n7. From 30 to 64 years\n8. From 35 to 49 years\n9. From 50 to 64 years\n10. From 65 to 74 years\n11. 16 years or over\n12. 65 years or over\n13. 75 years or over")
    return lista[int(input())-1]

def esFaltante(n):
    if n == True:
        n = 1
    else:
        n = 0
    return n

def reemplazarGuion(n):
    if n == "-":
        n = None
    return n