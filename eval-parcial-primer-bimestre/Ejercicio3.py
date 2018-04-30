# Realizar un programa que permita ingresar un valor en segundos, luego realizar un proceso que
# permita presentar el valor en minutos y segundos del valor dado.

def main():

    titulo_1 = "especificacion de minutos y segundos de un valor"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    segundos = int(input("Ingrese el valor en segundos: "))
    o1 = segundos // 60
    o2 = 60 * o1
    o3 = segundos - o2
    if o1 >= 1:
         print(segundos, "segundos es igual a", o1, "minutos y ", o3, "segundos.")
    else:
         print(segundos, "segundos es igual a", segundos, "segundos.")

main()
