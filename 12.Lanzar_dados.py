import random
def simulador_lanzamiento():
    """Simula el lanzamiento de dos dados y registra la frecuencia de cada suma (2 a 12) en 10,000 lanzamientos."""

    frecuencias = {i: 0 for i in range(2, 13)}


    for p in range(10000):
        dado1 = random.randint(1, 6)  # Lanzamiento del primer dado (entre 1 y 6)
        dado2 = random.randint(1, 6)  # Lanzamiento del segundo dado (entre 1 y 6)
        suma = dado1 + dado2  # Suma de los dos dados

        frecuencias[suma] += 1

    print("Reporte de frecuencias de las sumas de dos dados:")
    for suma, frecuencia in frecuencias.items():
        print(f"Suma {suma}: {frecuencia} veces")


if __name__ == "__main__":
    simulador_lanzamiento()
