def entradas_cine(sal: int) -> None:
    """Función para gestionar la compra de entradas de cine.

    Calcula el costo de una entrada, si es cliente o estudiante.

    Args:
        sal (int): Edad del cliente.
        estudiante (str): Indica si el cliente es estudiante ('s' para sí, 'n' para no).
    Returns:
        Y: Precio total de la entrada.
    """
    x=0

    estudiante, x = Validar_edad(sal, x)

    verificar_estudiante(estudiante, x)


def verificar_estudiante(estudiante, x):
    if estudiante.lower() == 's':
        z = x * 0.10
        print(f"Tiene un descuento de {z}")

        y = x - z
        print(f"El valor total de su entrada es: {y}")
    else:
        print("Pagas completo")


def Validar_edad(sal, x):
    if sal <= 12:
        x = 10000
        print(f"El valor total de su entrada es: {x}")
    elif sal > 12 and sal < 18:
        x = 15000
        print(f"El valor total de su entrada es: {x}")
    elif sal > 18:
        x = 20000
        print(f"El valor total de su entrada es: {x}")
    estudiante = input("¿Es usted estudiante? (s/n): ")
    return estudiante, x


if __name__ == "__main__":
    entradas_cine(sal=int(input("Indique su edad: ")))