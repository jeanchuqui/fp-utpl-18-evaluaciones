# Realizar un programa en Java que permita ingresar por teclado la longitud y la anchura de una
# habitación, realizar los procesos respectivos que permita obtener la superficie de la misma, además
# se debe presentar en pantalla el valor de la superficie, finalmente tomar en consideración que se
# debe presentar el valor con 3 decimales

def main():

    titulo_1 = "calculo de la  superficie de una habitacion"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    longitud = eval(input("Ingrese la longitud de la habitacion: "))
    ancho = eval(input("Ingrese el ancho de la habitacion: "))

    superficie = longitud * ancho

    print("La superficie de la habitacion es de: %.3f" % superficie, "metros cuadrados.")

main()
