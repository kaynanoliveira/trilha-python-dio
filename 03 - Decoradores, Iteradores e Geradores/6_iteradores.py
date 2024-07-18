carros = ["Fusca", "Jetta", "Ferrari", "Camaro"]

itCarros = iter(carros)

while itCarros:
    try:
        print(next(itCarros))

    except StopIteration:
        print("Fim da lista")

        break

