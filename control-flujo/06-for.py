# for numero in range(5):
#     print(numero, numero * 'hola mundo ')

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontré el número buscado")

for char in "Ultimate Python":
    print(char)