def suma_mayores(valor, lista):

    if len(lista) == 0:
        return 0

    primero = lista[0]
    if primero >= valor:
        return primero + suma_mayores(valor, lista[1:])
    else:
        return suma_mayores(valor, lista[1:])


numeros = [2, 5, 8, 1, 10, 3]
valor = 5
resultado = suma_mayores(valor, numeros)

print("La suma es:", resultado)