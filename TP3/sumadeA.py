def suma_hasta_A():
    A = int(input("Ingrese un número positivo: "))
    if A < 0:
        print("El número ingresado no es positivo. Por favor, intente de nuevo.")
        return
    suma = sum(range(1, A+1))
    print(f"La suma de los números desde 1 hasta {A} es {suma}")

suma_hasta_A()
