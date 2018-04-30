def main():

    titulo_1 = "que letra va primero"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    x = str(input("Ingrese una letra: "))
    y = str(input("Ingrese otra letra: "))
    z = str(input("Ingrese una última letra: "))

    v1 = x.upper()
    v2 = y.upper()
    v3 = z.upper()

    if v1 < v2 and v1 < v3:
        print("La primer letra que aparecce en el abecedario es: ", v1)
    elif v2 < v1 and v2 < v3:
        print("La primer letra que aparecce en el abecedario es: ", v2)
    else:
        print("La primer letra que aparecce en el abecedario es: ", v3)

main()