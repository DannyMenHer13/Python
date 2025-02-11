mensaje = f"""
Bienvenidos a la calculadora
Para salir escriba \"Salir\"
Las operaciones son suma, resta, multi y div
"""
operacion = ""
while operacion.lower() != "salir":
    n1 = input("Ingrese un numero: ")
    n1 = int(n1)
    operacion = input("Ingrese operacion: ")

    while operacion.lower() != "salir":
        if operacion.lower() == "suma":
            n2 = input("Ingrese otro numero: ")
            n2 = int(n2)
            resultado = n1 + n2
            print("El resultado es: ", resultado)
            n1 = resultado
        elif operacion.lower() == "resta":
            n2 = input("Ingrese otro numero: ")
            n2 = int(n2)
            resultado = n1 - n2
            print("El resultado es: ", resultado)
            n1 = resultado
        elif operacion.lower() == "multi":
            n2 = input("Ingrese otro numero: ")
            n2 = int(n2)
            resultado = n1 * n2
            print("El resultado es: ", resultado)
            n1 = resultado
        elif operacion.lower() == "div":
            n2 = input("Ingrese otro numero: ")
            n2 = int(n2)
            resultado = n1 / n2
            print("El resultado es: ", resultado)
            n1 = resultado
        else:
            print("Operación inválida.")
        
        operacion = input("Ingrese operacion: ")