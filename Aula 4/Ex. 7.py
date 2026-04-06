n = int(input("Tabuada de: "))
inicio = int(input("Começar tabuada por: "))
fim = int(input("Terminar tabuada em: "))

x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1