def es_palindromo(texto):
    num = 0
    nuevoTexto = ""
    texto2 = texto.replace(" ", "")
    for _ in texto2:
        num += 1
    while num > 0:
        nuevoTexto = nuevoTexto + texto2[num - 1]
        num -= 1
    if texto2.lower() == nuevoTexto.lower():
        return "es un palindromo"
    else:
        return "no es un palindromo"

print("Reconocer", es_palindromo("Reconocer"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Amo la paloma", es_palindromo("Amo la paloma"))