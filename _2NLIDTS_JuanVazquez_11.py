def suma_iterativa(n):
    suma = 0

    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n


def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10


def leer_entero(mensaje, minimo):
    """Lee un entero >= minimo, repitiendo hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
        except ValueError:
            pass
        except EOFError:
            # La entrada se cerro (Ctrl+D / Ctrl+Z): terminar sin error
            print("\n\nEntrada finalizada. Programa terminado.")
            raise SystemExit
        print(f"  Entrada invalida. Ingrese un numero entero mayor o igual a {minimo}.")


def mostrar_menu():
    print("\n=============================================")
    print("   SUMA DE LOS DIGITOS DE UN NUMERO NATURAL")
    print("=============================================")
    print("1. Calcular con la solucion iterativa")
    print("2. Calcular con la solucion recursiva")
    print("3. Calcular con ambas y comparar")
    print("0. Salir")
    print("---------------------------------------------")


def procesar_numeros(opcion):
    cantidad = leer_entero("\nCuantos numeros va a ingresar? ", 1)

    for i in range(1, cantidad + 1):
        n = leer_entero(f"Numero {i}: ", 0)

        if opcion == 1:
            print(f"  Suma de digitos (iterativa) de {n} = {suma_iterativa(n)}")
        elif opcion == 2:
            print(f"  Suma de digitos (recursiva) de {n} = {suma_recursiva(n)}")
        else:
            it = suma_iterativa(n)
            re = suma_recursiva(n)
            estado = "Resultados iguales" if it == re else "Resultados distintos"
            print(f"  Iterativa: {it} | Recursiva: {re}  -> {estado}")


def main():
    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = leer_entero("Elija una opcion: ", 0)

        if opcion in (1, 2, 3):
            procesar_numeros(opcion)
        elif opcion == 0:
            print("\nPrograma terminado. Hasta luego!")
        else:
            print("\nOpcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    main()
