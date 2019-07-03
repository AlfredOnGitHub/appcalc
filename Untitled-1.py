print("Bienvenido a la calculadora. Introduce el dígito de lo que quieres hacer. \n \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir")

while True:
    opcion = int(input("MENU: Introduzca opcion: "))
    if opcion == 1:
        a = int(input("SUMA: Introduce dígito: "))
        b = int(input("SUMA: Introduce otro dígito: "))
        suma = a + b
        print(suma)
    elif opcion == 2:
        a = int(input("RESTA: Introduce dígito: "))
        b = int(input("RESTA: Introduce otro dígito: "))
        resta = a - b
        print(resta)
    elif opcion == 3:
        a = int(input("MULTIPLICACIÓN: Introduce dígito: "))
        b = int(input("MULTIPLICACIÓN: Introduce otro dígito: "))
        mult = a*b
        print(mult)
    if opcion == 4:
        a = int(input("DIVISIÓN: Introduce dígito: "))
        b = int(input("DIVISIÓN: Introduce otro dígito: "))
        div = a/b
        print(div)
    elif opcion == 5:
        print("Gracias por usar la calculadora.")
        break
