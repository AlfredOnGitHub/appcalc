print("Bienvenido a la calculadora. Introduce el dígito de lo que quieres hacer. \n \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir")

while True:
    opcion = int(input("MENU: Introduzca opcion: "))
    if opcion == 1:
        try:
            a = int(input("SUMA: Introduce dígito: "))
            b = int(input("SUMA: Introduce otro dígito: "))
        except ValueError:
            print("Introduce un dígito, por favor. (Usted ha vuelto al menú.)")
        else:
            suma = a + b
            print(suma)
    elif opcion == 2:
        try:
            a = int(input("RESTA: Introduce dígito: "))
            b = int(input("RESTA: Introduce otro dígito: "))
        except ValueError:
            print("Introduce un dígito, por favor. (Usted ha vuelto al menú.)")
        else:
            resta = a - b
            print(resta)
    elif opcion == 3:
        try:
            a = int(input("MULTIPLICACIÓN: Introduce dígito: "))
            b = int(input("MULTIPLICACIÓN: Introduce otro dígito: "))
        except ValueError:
            print("Introduce un dígito, por favor. (Usted ha vuelto al menú.)")
        else:
            mult = a*b
            print(mult)
    if opcion == 4:
        try:
            a = int(input("DIVISIÓN: Introduce dígito: "))
            b = int(input("DIVISIÓN: Introduce otro dígito: "))
        except ValueError:
            print("Introduce un dígito, por favor. (Usted ha vuelto al menú.)")
        else:
            div = a/b
            print(div)
    elif opcion == 5:
        print("Gracias por usar la calculadora.")
        break
