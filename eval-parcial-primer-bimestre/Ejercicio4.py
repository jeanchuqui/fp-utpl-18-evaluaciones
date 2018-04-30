def main():

    titulo_1 = "sistema de ecuaciones"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    print("Dado el siguiente sistema de ecuaciones: \nax + by = c\ndx + ey = f")
    print("Se resolverá aplicando las siguientes fórmulas")
    print("x = (ce - bf)/(ae - bd)\ny = (ce - bf)/(ae - bd)")

    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    d = float(input("Ingrese el valor de d: "))
    e = float(input("Ingrese el valor de e: "))
    f = float(input("Ingrese el valor de f: "))

    x = ((c * e - b * f) / (a * e - b * d))
    y = ((c * e - b * f) / (a * e - b * f))


    print("Los valores de las variables (x) y (y) son:")
    print("x = ", x)
    print("y = ", y)


main()