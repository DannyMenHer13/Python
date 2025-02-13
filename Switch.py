from ClaseSwitch import switch
numero = 15

with switch(numero, comparator=lambda x , y: not x % y) as s:
    if s.case(2, True):
        print(f"{numero} es múltiplo de 2")
    if s.case(3, True):
        print(f"{numero} es múltiplo de 3")
    if s.case(5, True):
        print(f"{numero} es múltiplo de 5")
    if s.case(7, True):
        print(f"{numero} es múltiplo de 7")
    if s.default():
        print(f"{numero} no es múltiplo de 2, 3, 5 o 7")