# Realizar un programa que permita ingresar el número de mes de un año (1,…,12), en base al
# valor ingresado presenta el número de días que tiene ese mes.
def main():

    titulo_1 = "cantidad de días según el mes"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    mes = int(input("Ingrese el número del mes: "))

    if mes in [1,3,5,7,8,10,12]:
        dias = 31
        print("El mes", mes, "tiene", dias, "dias.")
    elif mes == 2:
        dias = 28
        print("El mes", mes, "tiene", dias, "dias.")
    elif mes in [4,6,9,11]:
        dias = 30
        print("El mes", mes, "tiene", dias, "dias.")
    else:
        print("El valor digitado no corresponde a ningun mes.")

main()
