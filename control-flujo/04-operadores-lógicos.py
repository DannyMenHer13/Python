# and, or, not

gas = True
encendido = True
edad = 18

# if not gas and (encendido or edad > 17):
#     print("Puedes avanzar")

# Operadores de corto circuito

if not gas and encendido and edad > 17:
    print("Puedes avanzar")