from ClaseSwitch import switch

peso = float(input("Ingrese su peso (en kilogramos): "))
altura = float(input("Ingrese su altura (en metros): "))

if peso <= 0 or altura <= 0:
    print("Valores ingresados inválidos.")
else:
    imc = round(peso / altura ** 2, 2)
    with switch(imc, comparator=lambda x, y: x < y) as s:
        if s.case(18.5, True):
            print(f"Su IMC es {imc}, tiene bajo peso.")
        if s.case(25, True):
            print(f"Su IMC es {imc}, tiene peso normal.")
        if s.case(30, True):
            print(f"Su IMC es {imc}, tiene sobrepeso.")
        if s.default():
            print(f"Su IMC es {imc}, tiene obesidad.")