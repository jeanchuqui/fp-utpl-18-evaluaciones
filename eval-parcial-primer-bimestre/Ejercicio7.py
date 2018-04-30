def main():

    titulo_1 = "sueldo total de un empleado en funcion de sus ventas"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    ventas = float(input("Ingrese ventas realizadas en el mes: $"))

    sueldo_fijo = 360.40

    if ventas <= 500:
        porc_ventas = ventas * 0.05
    elif ventas > 500 and ventas <= 1000:
        porc_ventas = ventas * 0.08
    elif ventas > 1000 and ventas <= 5000:
        porc_ventas = ventas * 0.1
    elif ventas > 5000:
        porc_ventas = ventas * 0.15
    else:
        print("El valor es incorrecto")

    sueldo_total = sueldo_fijo + porc_ventas

    print("Su sueldo total es de $", sueldo_total)

main()
