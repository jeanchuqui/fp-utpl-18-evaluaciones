def main():
    titulo_1 = "calculo de una operacion"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    print("Para calcular la siguiente operacion")
    print("m=(x+(y/z))/(x-(y/z)))")

    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    z = float(input("Ingrese el valor de z: "))

    m = ((x + (y / z)) / (x - (y / z)))

    print("El valor de m en base a las variables:\nx = ", x)
    print("y = ", y)
    print("z = ", z)
    print("da como resultado:\nm = ", m)


main()