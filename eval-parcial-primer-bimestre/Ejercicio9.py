def main():

    titulo_1 = "congruencia de 2 triángulos"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    print("Primer Triángulo:\n---elementos---\n\tLADOS:")

    l1_1 = float(input("Ingrese valor de un lado: "))
    l2_1 = float(input("Ingrese valor del otro lado: "))
    l3_1 = float(input("Ingrese valor del último lado: "))
    print("\tÁNGULOS:")
    a1_1 = float(input("Ingrese valor de un ángulo: "))
    a2_1 = float(input("Ingrese valor del otro ángulo: "))
    a3_1 = float(input("Ingrese valor del último ángulo: "))

    print("Segundo Triángulo:\n---elementos---\n\tLADOS:")

    l1_2 = float(input("Ingrese valor de un lado: "))
    l2_2 = float(input("Ingrese valor del otro lado: "))
    l3_2 = float(input("Ingrese valor del último lado: "))
    print("\tÁNGULOS:")
    a1_2 = float(input("Ingrese valor de un ángulo: "))
    a2_2 = float(input("Ingrese valor del otro ángulo: "))
    a3_2 = float(input("Ingrese valor del último ángulo: "))

    if l1_1 == l1_2 and l2_1 == l2_2 and l3_1 == l3_2:
        if a1_1 == a1_2 and a2_1 == a2_2 and a3_1 == a3_2:
            print("\nLos triángulos son congruentes.")
        else:
            print("\nLos ángulos no son congruentes.")
    else:
        print("\nLos ángulos no son congruentes.")

main()
