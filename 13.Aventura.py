def aventura():
    print("Te encuentras en un bosque y aparece una casa.")
    print("¿Qué te gustaría hacer?")
    print("1. Entrar en la casa")
    print("2. Buscar un camino de regreso")
    print("3. Acampar y descansar")

    while True:
        eleccion = input("Elige una opción (1, 2, o 3): ")

        if eleccion == "1":
            print("Dentro de la casa encuentras un tesoro escondido. ¡Felicidades!")
            break
        elif eleccion == "2":
            print("Había una bruja escondida y te raptó.")
            continuar = input("¿Quieres jugar de nuevo? (s/n): ")
            if continuar.lower() != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
        elif eleccion == "3":
            print("Descansas bien y al día siguiente encuentras un camino seguro de regreso a casa, "
                  "pero seguro te perdiste de algo.")
            continuar = input("¿Quieres jugar de nuevo? (s/n): ")
            if continuar.lower() != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
        else:
            print("Opción no válida. Intenta de nuevo.")

        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    aventura()
