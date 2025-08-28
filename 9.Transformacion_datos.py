def transformacion_datos(resultado):
    resultado = [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]

    trans=[{"nombre": item["nombre"], "precio": (item["precio"] * 0.19)+item["precio"]} for item in resultado]
    print(trans)

if __name__ == "__main__":
    transformacion_datos([])