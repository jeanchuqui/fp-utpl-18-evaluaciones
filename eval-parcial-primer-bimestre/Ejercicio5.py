def main():

    titulo_1 = "promedio y puntuacion de calificaciones de un estudiante"
    titulo_2 = titulo_1.upper()
    print(titulo_2)

    nota1 = float(input("Ingrese nota 1: "))
    nota2 = float(input("Ingrese nota 2: "))
    nota3 = float(input("Ingrese nota 3: "))
    nota4 = float(input("Ingrese nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4)/4

    if media >= 90 and media <= 100:
        puntuacion = "A"
    elif media >= 80 and media <= 89:
        puntuacion = "B"
    elif media >= 70 and media <= 79:
        puntuacion = "C"
    elif media >= 0 and media <= 69:
        puntuacion = "D"
    else:
        print("Error en el calculo del promedio.")

    print("El estudiante con el promedio de calificaciones", media, ", tiene una puntuacion de ", puntuacion)

main()
